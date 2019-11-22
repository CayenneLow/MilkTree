from flask import render_template, request, redirect, url_for, abort, session
from server import app
import requests

from models.project import Project
from models.Job import Job

# from freelancersdk.session import Session
# session = Session(oauth_token=2pMF6DNa7UUPSu9L83958IzrFBqWSp)

oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorize'
client_id = '16893251-7ef7-4c9c-8876-e7598f2e3569'
redirect_uri = 'http://localhost:5000/authorized'
prompt = 'select_account consent'
advanced_scopes = '1 2'
client_secret = 'ab7f65247142d1e36665020bb91dfad611b5152944b44c2e7a6ce8908356d67f1753a1544da4bc041715b50681688ec401d1e3dba9001420dc3e3f888a13332c'

# Gets system. 
def system():
    return app.config['SYSTEM']


@app.route('/')
def index():
    if 'access_token' in session:
        username = session['access_token']
        return ('Logged in as ' + username + '<br>' + \
         "<b><a href = '/clear'>click here to log out</a></b>"
         "<b><a href = '/testAPI'>click here to test api</a></b>")
    else:
        return render_template('base.html')


@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)

@app.route('/create-project', methods=['GET', 'POST'])
def create_project(title="", desc="", location=""):
    n_jobs = 0
    project = Project(title, desc)
    project.set_location(location)
    system().add_project(project)

    if (request.method == "POST"):
        title = request.form['title']
        desc = request.form['description']
        location = request.form['location']
        # Populate jobs for the project.
        for i in range(1, n_jobs):
            num_string = str(i)
            role = request.form[num_string + "-role"]
            job_desc = request.form[num_string + "-description"]
            budget = request.form[num_string + "-budget-price"]
            curr = request.form[num_string + "-budget-currency"]
            # TODO: Add skills here
            new_job = Job(i, role, job_desc, budget, curr) 
            project.add_job(new_job)
        
    return render_template('create_project.html', jobs = project.get_jobs(), njobs = n_jobs)

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
    payload = "grant_type=authorization_code&code={0}&client_id={1}&client_secret={2}&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fauthorized".format(code, client_id, client_secret)
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    # print(response)
    response = response.json()

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
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/projects')
def singleProject():
    #code = request.args.get('code')
    # print(id)
    return render_template('individualProject.html')

