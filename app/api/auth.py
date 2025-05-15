from flask import Blueprint, jsonify, request, current_app
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
from app.models import User
from dotenv import load_dotenv
from app import db
import os
from . import api_bp

load_dotenv()

key = os.getenv('SECRETKEY')
cipher_suite = Fernet(key.encode('utf-8'))

def check_password(userToken, token):
    # Decrypt the password
    print(userToken)
    tokenBits = token.encode('utf-8')
    decrypted_token = cipher_suite.decrypt(userToken)
    # Compare the decrypted password with the provided password
    print("decrypted_password: ", decrypted_token)
    print("passwordBits: ", tokenBits)
    return decrypted_token == tokenBits
    

@api_bp.post('/login')
def login():
    body = request.get_json()
    ip = body['ip']
    token = body['token']

    user = User.query.filter_by(ip=ip).first()

    try:    
        headers =  {"Authorization": "Bearer "+ token}
        api_url = "https://"+ ip + ":6443" +"/api"
        print(api_url)
        response = requests.get(api_url, headers=headers, verify=False)
        if response.status_code == 401:
            return jsonify({"status": "error", "message": "Invalid token"}), 401
    except:
        return jsonify({"status": "error", "message": "No route to host"}), 500

    if not user:
        new_user = User(ip=ip, token=cipher_suite.encrypt(token.encode('utf-8')))
        db.session.add(new_user)
        db.session.commit()
    if user and not check_password(user.token, token):
        user.token = cipher_suite.encrypt(token.encode('utf-8'))
        db.session.commit()
    
    current_app.config['KUBERNETES_IP'] = ip
    current_app.config['TOKEN'] = token

    return jsonify({'message': 'Valid Token'}), 200


@api_bp.get('/users')
def getUsers():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'ip': user.ip}
        output.append(user_data)
    return jsonify({'users': output})

@api_bp.post('/autoLogin')
def autoLogin():
    body = request.get_json()
    ip = body['ip']

    user = User.query.filter_by(ip=ip).first()

    token = cipher_suite.decrypt(user.token).decode('utf-8')

    try:    
        headers =  {"Authorization": "Bearer "+ token}
        api_url = "https://"+ ip + ":6443" +"/api"
        response = requests.get(api_url, headers=headers, verify=False)
        if response.status_code == 401:
            return jsonify({"status": "error", "message": "Invalid token"}), 401
    except:
        return jsonify({"status": "error", "message": "No route to host"}), 500


    current_app.config['KUBERNETES_IP'] = ip
    current_app.config['TOKEN'] = token

    return jsonify({'message': 'Login successful'}), 200

@api_bp.get('/logout')
def logout():
    current_app.config['KUBERNETES_IP'] = None
    current_app.config['TOKEN'] = None
    return jsonify({'message': 'Logout successful'}), 200