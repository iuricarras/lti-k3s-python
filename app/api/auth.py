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

def check_password(userPassword, password):
    # Decrypt the password
    passwordBits = password.encode('utf-8')
    decrypted_password = cipher_suite.decrypt(userPassword)
    # Compare the decrypted password with the provided password
    print("decrypted_password: ", decrypted_password)
    print("passwordBits: ", passwordBits)
    return decrypted_password == passwordBits
    

@api_bp.post('/login')
def login():
    body = request.get_json()
    ip = body['ip']
    username = body['username']
    password = body['password']

    user = User.query.filter_by(ip=ip).first()

    if user and not check_password(user.password, password): # if a user is found, we want to redirect back to signup page so user can try again
        return jsonify({'message': 'Invalid credentials'}), 401
    elif user and check_password(user.password, password):
        current_app.config['ROUTER_IP'] = ip
        current_app.config['AUTHENTICATION'] = (username, password)
        print(f"routerip set to: {current_app.config['ROUTER_IP']}")
        return jsonify({'message': 'Login successful'}), 200
    
    try:    
        auth = (username, password)
        api_url = "http://"+ ip +"/rest"
        response = requests.get(api_url, auth=auth)
        if response.status_code == 401:
            return jsonify({"status": "error", "message": "Invalid credentials"}), 401
    except:
        return jsonify({"status": "error", "message": "No route to host"}), 500
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(ip=ip, username=username, password=cipher_suite.encrypt(password.encode('utf-8')))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    current_app.config['ROUTER_IP'] = ip
    current_app.config['AUTHENTICATION'] = (username, password)

    return jsonify({'message': 'User created successfully'}), 201


@api_bp.get('/users')
def getUsers():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'ip': user.ip, 'username': user.username}
        output.append(user_data)
    return jsonify({'users': output})

@api_bp.post('/autoLogin')
def autoLogin():
    body = request.get_json()
    ip = body['ip']

    user = User.query.filter_by(ip=ip).first()

    current_app.config['ROUTER_IP'] = ip
    current_app.config['AUTHENTICATION'] = (user.username, cipher_suite.decrypt(user.password).decode('utf-8'))

    return jsonify({'message': 'Login successful'}), 200

@api_bp.get('/logout')
def logout():
    current_app.config['ROUTER_IP'] = None
    current_app.config['AUTHENTICATION'] = None
    return jsonify({'message': 'Logout successful'}), 200