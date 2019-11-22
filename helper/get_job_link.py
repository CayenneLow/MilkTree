from flask import session
import requests

oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorize'
client_id = '0a75d1eb-cbb4-40ce-9e1e-7419f780ff13'
redirect_uri = 'https://localhost:5000/authorized'
prompt = 'select_account consent'
advanced_scopes = '1 2'
client_secret = 'f6e934fbdfde41364ffcf14a6ca5aa991bbfe376414ff3397a9d0ad507d8ecf88ccc5e9a6ead35eec80daf4a24ca2f13a93115ddcd7ddf6e34bf69d6ae68750c'

def get_job_link():
    headers = {'content-type': 'application/json', 'freelancer-oauth-v1': session['access_token']}
    url = 'https://www.freelancer-sandbox.com/api/projects/0.1/projects/all/'
    
    response = requests.request("GET", url, headers=headers).json()
    return response["result"]["seo_url"]