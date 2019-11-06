#!/usr/bin/python3
import sys
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class MyWatson():
    def __init__(self,)
    def make(api,zip_path = "./img/myself.zip"):

        with open(zip_path, 'rb') as myself, open("./img/bear.zip", 'rb') as bear:
             model = api.create_classifier(
                'denkiguma',
                positive_examples={'myself': myself, 'bear': bear}).get_result()
             return json.dumps(model, indent=2)

def ls(api):
    result = api.list_classifiers(verbose=True).get_result()
    return result

def rm(api,del_id):
    api.delete_classifier(del_id)

def judge(api,model,img):
    result = api.classify(url=img,
        classifier_ids=[model]).get_result()
    return result

def getAPI():
    with open("watson.key") as key:
        auth = IAMAuthenticator(key.read().strip())
    api = VisualRecognitionV3(
        version='2018-03-19',
        authenticator=auth
    )
    return api

if __name__ == '__main__':
    api = getAPI()

    opt = sys.argv[1]
    if opt == "make":
        print(make(api,sys.argv[2]))
    if opt == "ls":
        print(json.dumps(ls(api),indent=2))
    if opt == "rm":
        rm(api,sys.argv[2])
    if opt == "judge":
        print(judge(api,sys.argv[2],sys.argv[3]))

