'''file where all routes of flask app are available'''
from app import app
from flask import Flask, redirect, url_for, render_template, request ,session,g,make_response
import requests  
import json
import os  

@app.route('/')
def OnSearch():
    json_args = json.loads(request.data)
    data = str(json_args)
    with open("sample.txt", "w") as outfile:
        outfile.write(data)
    return json_args

@app.route('/searchinternal',methods = ['post'])
def SearchInternal():
    data = "{\"message\":{\"intent\":{\"fulfillment\":{\"type\":\"Teleconsultation\",\"agent\":{\"name\":\"mohit\"},\"start\":{\"time\":{\"timestamp\":\"2022-07-14T13:24:20\"}},\"end\":{\"time\":{\"timestamp\":\"2022-07-14T23:59:59\"}}}}},\"context\":{\"domain\":\"nic2004:85111\",\"country\":\"IND\",\"city\":\"std:080\",\"action\":\"search\",\"timestamp\":\"2022-07-14T08:05:55.252760Z\",\"core_version\":\"0.7.1\",\"consumer_id\":\"eua-nha\",\"consumer_uri\":\"http://100.96.9.173:8080/api/v1/euaService\",\"transaction_id\":\"c8f9ad70-034b-11ed-a6d6-c13d491ee158\",\"message_id\":\"c8f9ad70-034b-11ed-a6d6-c13d491ee158\"}}"
    headers = {'Content-Type':'application/json'}
    request_body = requests.post('http://121.242.73.120:8083/api/v1/search',headers=headers,data = data)
    json_args = json.loads(request.data)
    path = ""
    if os.path.exists(f'{path}/sample.txt'):
        return json_args
    else:
        time.sleep()
    return json_args
