from flask import redirect, url_for, session
import requests
import json 
from models.Job import Job

oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorize'
client_id = '0a75d1eb-cbb4-40ce-9e1e-7419f780ff13'
redirect_uri = 'https://localhost:5000/authorized'
prompt = 'select_account consent'
advanced_scopes = '1 2'
client_secret = 'f6e934fbdfde41364ffcf14a6ca5aa991bbfe376414ff3397a9d0ad507d8ecf88ccc5e9a6ead35eec80daf4a24ca2f13a93115ddcd7ddf6e34bf69d6ae68750c'


# Creates a new JSON Object for a job to post to freelancer.
def create_new_job_json(job):
    job_dict = {
        "title": job.get_title(),
        "description": job.get_description(),
        "currency": {
            "id": job.get_currency(),
        },
        "budget": {
            "minimum": job.get_budget_min(),
            "maximum": job.get_budget_max(),
        },
        "jobs": job.get_skills() # skills 
        
    }

    return json.dumps(job_dict)


# Posts a project in freelancer.
def post_job(job):
    # TODO: parse into correct json format ``
    job_json = create_new_job_json(job)
    headers = {'content-type': 'application/json', 'freelancer-oauth-v1': session['access_token']}
    url = 'https://www.freelancer-sandbox.com/api/projects/0.1/projects/'
    
    response = requests.request("POST", url, data=job_json, headers=headers).json()
    return response