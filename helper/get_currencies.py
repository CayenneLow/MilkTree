import requests
from flask import session

# Gets currencies from freelancer api
def get_currencies():
    url = 'https://www.freelancer-sandbox.com/api/projects/0.1/currencies/'
    
    response = requests.request("GET", url).json()
    return response["result"]