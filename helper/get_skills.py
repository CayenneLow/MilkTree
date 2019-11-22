from flask import redirect, url_for, session
import requests

def get_skills():
    url = 'https://www.freelancer.com/api/projects/0.1/jobs/search/'
    response = requests.request("GET", url).json()
    skills = response["result"]
    return skills