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
        ubigeo = ubigeo_dic[str(mark['ubigeo']).zfill(6)]

        ubigeo_str = f"{ubigeo['name']} - {ubigeo['city']} ({ubigeo['state']})"

        if ubigeo_str in marks_dic:
            marks_dic[ubigeo_str] +=  1
        else:
            marks_dic[ubigeo_str] = 1
    
    sorted_dict = {k: marks_dic[k] for k in sorted(marks_dic, key=marks_dic.get, reverse = True)}
    
    print("\n")
    for k in sorted_dict: 
        name, reference = k.split("-")
        print(f"\t {str(sorted_dict[k]).rjust(8)} | {name.ljust(30)} | {reference}")
    print("\n")

 