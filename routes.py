from flask import render_template, request, redirect, url_for, abort, session
from server import app
import requests

from models.Project import Project
from models.Job import Job

# from freelancersdk.session import Session
# session = Session(oauth_token=2pMF6DNa7UUPSu9L83958IzrFBqWSp)

oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorize'
client_id = '0a75d1eb-cbb4-40ce-9e1e-7419f780ff13'
redirect_uri = 'https://localhost:5000/authorized'
prompt = 'select_account consent'
advanced_scopes = '1 2'
client_secret = 'f6e934fbdfde41364ffcf14a6ca5aa991bbfe376414ff3397a9d0ad507d8ecf88ccc5e9a6ead35eec80daf4a24ca2f13a93115ddcd7ddf6e34bf69d6ae68750c'

def system():
    return app.config['SYSTEM']

@app.route('/')
def index():
    if 'access_token' in session:
        username = session['access_token']
        return ('Logged in as ' + username + '<br>' + \
         "<b><a href = '/clear'>click here to log out</a></b>")
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
    if (request.method == "POST"):
        title = request.form['title']
        desc = request.form['description']
        location = request.form['location']
        # Populate jobs for the project.
        jobs = []
        for i in range(1, n_jobs):
            num_string = str(i)
            role = request.form[num_string + "-role"]
            job_desc = request.form[num_string + "-description"]
            budget = request.form[num_string + "-budget-price"]
            curr = request.form[num_string + "-budget-currency"]
            # TODO: Add skills here
            new_job = Job(i, role, job_desc, budget, curr)
            jobs.append(new_job)
        
    project = Project(title, desc)
    project.set_location(location)
    project.set_jobs(jobs)
    system().add_project(project)

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

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
