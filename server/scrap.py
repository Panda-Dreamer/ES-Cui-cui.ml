EBirdAPIKEY = "s08bvu01hv7h"
from cmath import pi
from requests import request
from bs4 import BeautifulSoup
from google_trans_new import google_translator  

translator = google_translator()
def debugLog(info,msg,status):
    if(status == True):
        print('{} -- {}'.format(info,msg))

def get_info(code, debug):
    link = "https://ebird.org/species/"+code+"?locale=fr"
    r = request(method='GET', url=link)
    try:
        soup = BeautifulSoup(r.text, 'html.parser')
        list = soup.find_all("div", {"class": "MediaThumbnail Media--playButton"})
        if(len(list) >= 1):
            imageDIV1 = str(soup.find_all("div", {"class": "MediaThumbnail Media--playButton"})[0]).split("src")[1].split("\"")[1]
        else:
            imageDIV1 = ""
        
        if(len(list) >= 2):
            imageDIV2 = str(soup.find_all("div", {"class": "MediaThumbnail Media--playButton"})[1]).split("src")[1].split("\"")[1]
        else:
            imageDIV2 = ""

        if(len(list) >= 3):
            imageDIV3 = str(soup.find_all("div", {"class": "MediaThumbnail Media--playButton"})[2]).split("src")[1].split("\"")[1]
        else:
            imageDIV3 = ""

        if(len(str(soup.find_all("p", {"class": "u-stack-sm"})).split(">")) >= 1):
            desc_en = str(soup.find_all("p", {"class": "u-stack-sm"})).split(">")[1].split("<")[0]
            desc= translate(desc_en, debug).replace("'", " ")
        else:
            desc_en = ""
            desc = "Erreur lors de la récupération de la description"
        return {'status': True, 'images': [imageDIV1,imageDIV2,imageDIV3], 'desc': desc, 'desc_en': desc_en}
    except Exception  as e:
        debugLog("Html Parsing", str(e), debug)
        return {'status':False,'message':'Could not parse html from result, error: {}'.format(str(e))}



def translate(string, d):
    try:
        text = translator.translate(string.replace("\n",""),lang_tgt='fr').encode("utf-8").decode("utf-8").replace('\r', '').replace('\n', '')
        debugLog("TranslationText",text,d)  
        return text
    except Exception  as e:
        debugLog("Translation",str(e), d)    