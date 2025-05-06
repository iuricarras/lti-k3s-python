import requests
from flask import current_app
import json

def apiRequest(url, method, body=None):
    routerip = "localhost:8001"  # Replace with your router's IP address
    #authentication = current_app.config.get('AUTHENTICATION')
    api_url = "http://"+ routerip + url
    if method == 'GET':
        response = requests.get(api_url)
    elif method == 'POST':
        response = requests.post(api_url, data=json.dumps(body), headers={'content-type':'application/json'})
    elif method == 'PUT':
        response = requests.put(api_url, data=json.dumps(body), headers={'content-type':'application/json'})
    elif method == 'PATCH':
        response = requests.patch(api_url, data=json.dumps(body), headers={'content-type':'application/json'})
    elif method == 'DELETE':
        response = requests.delete(api_url)
    return response.json(), response.status_code