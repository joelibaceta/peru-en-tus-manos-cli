import requests
import os
import json
from datetime import datetime

baseuri = "https://us-central1-cadi360-sac.cloudfunctions.net/function-pakipe-publish/api/v1/"

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
    'K-Device': '5a5e1120-e245-45b2-8dda-5cef9e3ebb91'
}

def getSummary(date=None):
    if not date:
        date = datetime.strftime("%d-%m-%Y")
    response = requests.get(baseuri + "/summary/peru", params={'date': date}, headers= headers)



def getLocationSummary():

    ubigeo_data = open(os.getcwd() + "/ubigeo_data")
    ubigeo_dic = json.load(ubigeo_data)

    marks_dic = {}

    response = requests.get(baseuri + "/marks", headers= headers)

    marks = response.json()

    for mark in marks:
        ubigeo = str(mark['ubigeo']).zfill(6)
        if ubigeo in marks_dic:
            marks_dic[ubigeo] +=  1
        else:
            marks_dic[ubigeo] = 0
    
    
getLocationSummary()
 