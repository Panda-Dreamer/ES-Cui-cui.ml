from email.mime import audio
import analyze
import scrap
import datetime
import gevent
import uuid
from pydub import AudioSegment
# celery -A tasks worker --loglevel=info

def makeConfig(debug):
    settings = {
        'LATITUDE':-1,
        'LATITUDE' : -1,
        'LONGITUDE' : -1,
        'WEEK' : -1,
        'SIGMOID_SENSITIVITY' : 1.0,
        'LOCATION_FILTER_THRESHOLD' : 0.03,
        'LABELS_FILE' : './Files/Labels.txt',
        'CODES_FILE' : './Files/Codes.json',
        'SPECIES_FILE' : './Files/SpeciesList.json',
        'FR_LABELS_FILES' : './Files/Labels_FR.txt',
        'Debug': debug,
        'BATCH_SIZE' : 1,
        'SAMPLE_RATE':48000,
        'SIG_LENGTH':3.0,
        'SIG_MINLEN':3.0,
        'SIG_OVERLAP':0,
        'LABELS':[],
        'CODES':[],
        'FR_LABELS':{},
        'nresult':4
    }



    return settings

def analyse(audio_path, debug, complete, idOnly):
    if( not audio_path.split(".")[1] == "wav"):
        sound = AudioSegment.from_file(audio_path)
        sound.export(audio_path.split(".")[0]+".wav", format="wav")
    config = makeConfig(debug)
    results = analyze.analyzeFile(audio_path, config)
    if(complete == True and results['status']==True):
        data1 = results['results']
        for result in data1:
            data = scrap.get_info(result['specie_code'], debug)
            print("Status:", data['status'])
            if(data['status'] == True):
                result['images'] = data['images']
                result['desc'] = data['desc']
                result['desc_en'] = data['desc_en']
            else:
                result['images'] = ["","",""]
                result['desc'] = "Erreur lors de la récupération de la description"
        results['results'] = data1
    if idOnly == False:
        return results
    else:
        uuidp = str(uuid.uuid4())
        newresults = transformator(results)
        with open('./storage/{}-data.txt'.format(uuidp), 'w') as fp:
            fp.write(str(newresults))
        return {'status':True,'uuid':uuidp}

def transformator(results):
    r = results['results']
    print("r:",r)
    newobj = {
        'len':len(r),
    }
    index = 1
    for i in r:
        if(i['FR_label'] == "Not found"):
            newobj['name_{}'.format(index)] = i['label'].split("_")[0].replace("'","")
        else:
            newobj['name_{}'.format(index)] = i['FR_label'].split("_")[1].replace("'","")
        newobj['desc_{}'.format(index)] = i['desc'].replace("«","").replace("»","").replace("\"","")

        newobj['specie_{}'.format(index)] = i['specie_name'].replace("'","")

        newobj['image_{}_1'.format(index)] =  i['images'][0]
        newobj['image_{}_2'.format(index)]=i['images'][1]
        newobj['image_{}_3'.format(index)]=i['images'][2]
        newobj['conf_{}'.format(index)]=float(i['confidence']) * 100
        index=index+1
    return newobj
    

def getDesc(codes):
    results = {}
    for code in codes:
        result = scrap.get_info(code)
        results[code] = result
    return results
    

def testSync():
    stime = datetime.datetime.now().time()
    gevent.sleep(10)
    etime = datetime.datetime.now().time()
    return {'status':True,'message':'Test sync, started:{}, ended:{}'.format(stime,etime)}


def getResult(id):
    try:
        with open('storage/{}-data.txt'.format(id)) as file:
            lines = file.readlines()
            return lines[0]
    except Exception as e:
        print(e)
        return {'status':False,'message':'No result found for id:{}, Erreur: {}'.format(id,str(e))}
