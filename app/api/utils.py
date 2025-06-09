import requests
from flask import current_app
import json

def apiRequest(url, method, body=None):
    k3sip = current_app.config.get('KUBERNETES_IP')
    print(k3sip)
    api_url = "https://"+ k3sip + ":6443" + url
    headers = {"Authorization": "Bearer " + current_app.config.get('TOKEN')}
    print(headers)
    if method == 'GET':
        response = requests.get(api_url, headers=headers, verify=False)
    elif method == 'POST':
        response = requests.post(api_url, data=json.dumps(body), headers=headers, verify=False)
    elif method == 'PUT':
        response = requests.put(api_url, data=json.dumps(body), headers=headers, verify=False)
    elif method == 'PATCH':
        response = requests.patch(api_url, data=json.dumps(body), headers=headers, verify=False)
    elif method == 'DELETE':
        response = requests.delete(api_url, headers=headers, verify=False) 
    return response.json(), response.status_code