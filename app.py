from flask import Flask, jsonify, request, abort, redirect, url_for, render_template
from models import db, Gene, RSNum
from sqlalchemy.sql.expression import func, text
from datetime import datetime
import logging
from requests_oauthlib import OAuth2Session
from lib import me
from settings import API_credentials

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sexy_project.db'
 

PORT=5000


db.init_app(app)
db.create_all(app=app)

client_id = API_credentials['id']
client_secret = API_credentials['secret']
redirect_uri = 'http://localhost:5000/receive_code/'
API_TOKEN_URL = 'https://api.23andme.com/token/'
API_AUTH_URL = 'https://api.23andme.com/authorize/'
scopes = ['basic', 'names', 'email', 'genomes', 'report:all', 'phenotypes:read:all']

access_token = ''

@app.route('/')
def index():
    ttam_oauth = OAuth2Session(client_id,
                               redirect_uri=redirect_uri,
                               scope=scopes)
    auth_url, state = ttam_oauth.authorization_url(API_AUTH_URL)
    return render_template('index.html', auth_url=auth_url)

@app.route('/receive_code/')
def receive_code():
    global access_token
    ttam_oauth = OAuth2Session(client_id,
                               redirect_uri=redirect_uri)
    token_dict = ttam_oauth.fetch_token(API_TOKEN_URL,
                                        client_secret=client_secret,
                                        authorization_response=request.url)

    access_token = token_dict['access_token']

    return(redirect(url_for('home')))

@app.route('/home')
def home():
    account = me.get_account(access_token).json()
    if 'error' in account:
        return redirect(url_for('index'))

    profile = me.get_profile(account['data'][0]['profiles'][0]['id'], access_token).json()
    print(profile)

    return render_template('home.html', first_name=account['data'][0]['first_name'], last_name=account['data'][0]['last_name'], reports=profile['data'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
