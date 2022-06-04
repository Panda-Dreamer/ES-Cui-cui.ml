import os
import bottle
import argparse
import uuid
from requests import request
import base64
from tasks import * 
from bottle import response
import json
#from gevent import monkey; monkey.patch_socket()

@bottle.route('/<:re:.*>', method='OPTIONS')
def enable_cors_generic_route():
    add_cors_headers()

@bottle.hook('after_request')
def enable_cors_after_request_hook():
    add_cors_headers()

def add_cors_headers():
      bottle.response.headers['Access-Control-Allow-Origin'] = '*'
      bottle.response.headers['Access-Control-Allow-Methods'] = \
            'GET, POST, PUT, OPTIONS'
      bottle.response.headers['Access-Control-Allow-Headers'] = \
            'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'




@bottle.route('/api/healthcheck', method='GET')
def healthcheck():

    data = """Server CUI-CUI.ml<br>
    <br>
    /api/healthcheck GET<br>
    returns this page<br>
    <br>
    /api/analyse POST body:{"audio":"base64","complete":true/false}<br>
    returns an array of objects with the following structure:<br>
    {<br>
    "specie_code":"code",<br>
    "specie_name":"name",<br>
    "confidence":0.0,<br>
    "images":[<br>
    "url1",<br>
    "url2",<br>
    ...<br>
    ],<br>
    "desc":"description"<br>
    "FR_label":"label in french"<br>
    }<br>
    <br>
    /api/get-bird GET ?code=[code]<br>
    returns an object with the following structure:<br>
    {<br>
    "images":[<br>
    "url1",<br>
    "url2",<br>
    ...<br>
    ],<br>
    "desc":"description"<br>
    }<br>
    """
    return data

@bottle.route('/api/testSync', method='GET')
def handleRequest():
    print("Starting .delay()")
    result = testSync()

@bottle.route('/api/analyze', method='POST')
def handleRequest():
    print("Received analyse")
    Isjson = False
    upload = bottle.request.files.get('audio')
    idOnly = True
    if(not upload):
        body = bottle.request.json
        if( not body):
            return {'status':False,'message':'Could not get body from request !'}
        else:
            if(not (isinstance(body['complete'],bool) and isinstance(body['audio'],str))):
                return {'status':False,'message':'Complete and audio must be boolean and string !'}
            Isjson = True
            audio_encoded = body['audio']
            complete = body['complete']
            extension = "wav"
    else:
        extension = upload.filename.split('.')[1]

    if(not upload and not Isjson):
        return {'status':False,'message':'No file uploaded'}
    
    thread_uuid = str(uuid.uuid4())
    path = "./transfer/{}.{}".format(thread_uuid+"-sound",extension)

    if(Isjson == False):
        upload.save(path)
        complete = True
    else:
        wav_file = open(path, "wb")
        try:
            decode_string = base64.b64decode(audio_encoded)
            wav_file.write(decode_string)
        except Exception as e:
            return {'status':False,'message':'Could not decode base64 string !, error: {}'.format(str(e))}
    
    size = os.path.getsize(path)
    if(size > 5e+8):
        return {'status':False,'message':'File size is too big (size: {}B, limit:500MB)'.format(size)}

    result = analyse(path, args.debug, complete, idOnly)
    try:
        os.remove(path)
    except:
        pass
    return result

@bottle.route('/api/get-bird', method='GET')
def handleRequest():
    specie = bottle.request.query["code"]
    if(not specie):
        return {'status':False,'message':'No specie code provided'}
    
    result = getDesc([specie])
    return result

@bottle.route('/api/get-results', method='GET')
def handleRequest():
    id = bottle.request.query["code"]
    if(not id):
        return {'status':False,'message':'No token provided'}
    
    result = getResult(id).replace("'","\"")

    return result
   


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API endpoint server to analyze files remotely.')
    parser.add_argument('--host', default='0.0.0.0', help='Host name or IP address of API endpoint server. Defaults to \'0.0.0.0\'')   
    parser.add_argument('--port', type=int, default=3000, help='Port of API endpoint server.')   
    parser.add_argument('--debug', type=bool, default=False, help='Enable debug mode.')

    args = parser.parse_args()

    # Load translated labels
    print('UP AND RUNNING! LISTENING ON {}:{}'.format(args.host, args.port), flush=True)
    bottle.run(host=args.host, port=args.port, quiet=True, server='paste')