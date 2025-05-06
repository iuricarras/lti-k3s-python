import os
from flask import Blueprint, current_app, send_file

client_bp = Blueprint('client_app', __name__,
                      url_prefix='',
                      static_url_path='',
                      static_folder='./dist/assets/',
                      template_folder='./dist/',
                      )

@client_bp.route('/', defaults={'path': ''})
@client_bp.route('/<path>')
@client_bp.route('/<path>/<string>')
def index_client(path, string=None):
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)

@client_bp.route('/favicon.ico')
def favicon():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'favicon.ico')
    return send_file(entry)