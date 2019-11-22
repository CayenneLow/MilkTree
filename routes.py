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
         "<b><a href = '/clear'>click here to log out</a></b>"
         "<b><a href = '/testAPI'>click here to test api</a></b>")
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

@app.route('/testAPI')
def testAPI():
    headers = {'content-type': 'application/json', 'freelancer-oauth-v1': session['access_token']}
    url = 'https://www.freelancer-sandbox.com/api/projects/0.1/projects/'
    payload = '{"title": "Fix my PHP website",  "description": "I wrote a small website in PHP but it does not work. I need someone to fix it.",  "currency": {"id": 3},"budget": {"minimum": 250, "maximum": 500},"jobs": [{"id": 3},{"id": 17}]}'
    
    response = requests.request("POST", url, data=payload, headers=headers).json()
    print(response)
    return redirect(url_for("index"))
    

"""
    curl -X POST \
https://www.freelancer.com/api/projects/0.1/projects/ \
--header 'freelancer-oauth-v1: <oauth_access_token>' \
--header 'Content-Type: application/json' \
--data '{
  "title": "Build my Super Website!",
  "description": "project description",
  "currency": {
    "id": 1
  },
  "budget": {
    "minimum": 20.5,
    "maximum": 80.5,
    "currency_id": 1
  },
  "jobs": [
    {
      "id": 7
    }
  ],
  "type": "FIXED",
  "hourly_project_info": {
    "commitment": {
      "hours": 1,
      "interval": "WEEK"
    }
  },
  "hireme": true,
  "hireme_initial_bid": {
    "bidder_id": 1,
    "amount": 12.2,
    "period": 7
  },
  "location": {
    "city": "Sydney",
    "country": {
      "name": "Australia",
      "flag_url": "null",
      "code": "null",
      "highres_flag_url": "null",
      "flag_url_cdn": "null",
      "highres_flag_url_cdn": "null"
    },
    "latitude": 1,
    "longitude": 1,
    "administrative_area": "Hello, world!",
    "full_address": "Hello, world!",
    "vicinity": "Hello, world!"
  }
}'
"""