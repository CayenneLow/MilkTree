from flask import render_template, request, redirect, url_for, abort, session
from server import app
import requests
# from freelancersdk.session import Session
# session = Session(oauth_token=2pMF6DNa7UUPSu9L83958IzrFBqWSp)

oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorize'
client_id = '0a75d1eb-cbb4-40ce-9e1e-7419f780ff13'
redirect_uri = 'https://localhost:5000/authorized'
prompt = 'select_account consent'
advanced_scopes = '1 2'
client_secret = 'f6e934fbdfde41364ffcf14a6ca5aa991bbfe376414ff3397a9d0ad507d8ecf88ccc5e9a6ead35eec80daf4a24ca2f13a93115ddcd7ddf6e34bf69d6ae68750c'


@app.route('/')
def index():
    if 'access_token' in session:
        username = session['access_token']
        return ('Logged in as ' + username + '<br>' + \
         "<b><a href = '/clear'>click here to log out</a></b>")
    else:
        return render_template('base.html')

# Users who hit this endpoint will be redirected to the authorization prompt
@app.route('/authorize')
def handle_authorize():
    return redirect(
        '{0}?response_type=code'
        '&client_id={1}&redirect_uri={2}'
        '&scope=basic&prompt={3}'
        '&advanced_scopes={4}'.format(
            oauth_uri, client_id, redirect_uri, prompt, advanced_scopes
        )
    )

@app.route('/authorized')
def authorized():
    url = "https://accounts.freelancer-sandbox.com/oauth/token"
    code = request.args.get('code')
    print(code)
    payload = "grant_type=authorization_code&code={0}&client_id={1}&client_secret={2}&redirect_uri=https%3A%2F%2Flocalhost%3A5000%2Fauthorized".format(code, client_id, client_secret)
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers).json()

    # print(response.text)
    session["access_token"] = (response["access_token"])
    session["refresh_token"] = (response["refresh_token"])
    return redirect(url_for("index"))

@app.route("/clear")
def clear_token():
    """Removes the current OAuth access token locally."""
    session.pop("access_token", None)
    session.pop("refresh_token", None)
    return redirect(url_for("index"))

@app.route('/login')
def login():
    return render_template('login.html')
