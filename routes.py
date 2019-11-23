from flask import render_template, request, redirect, url_for, abort, session
from server import app
import requests
import json

from models.project import Project
from models.Job import Job
from helper.post_job import post_job

# from freelancersdk.session import Session
# session = Session(oauth_token=2pMF6DNa7UUPSu9L83958IzrFBqWSp)

oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorize'
client_id = '16893251-7ef7-4c9c-8876-e7598f2e3569'
redirect_uri = 'http://localhost:5000/authorized'
prompt = 'select_account consent'
advanced_scopes = '1 2'
client_secret = 'ab7f65247142d1e36665020bb91dfad611b5152944b44c2e7a6ce8908356d67f1753a1544da4bc041715b50681688ec401d1e3dba9001420dc3e3f888a13332c'

# slack stuff
oauth_token = "xoxp-833602236162-846395388917-845932523860-ec230dbd17792319cea682d78abdb604"

# Gets system.
def system():
    return app.config['SYSTEM']

# Gets the skills as a json.
def get_skills():
    return app.config['SKILLS']

# Gets currencies as a json.
def get_currencies():
    return app.config['CURRENCIES']

def get_curr_id(curr, currency_result):
    for currency in currency_result['currencies']:
        if currency['code'] is curr:
            return currency['id']

def get_skill_id(skill, skills_result):
    for skill_i in skills_result:
        if skill_i['name'] == skill:
            return skill_i['id']

@app.before_request
def before_request():
    if '/static/' not in request.path and request.endpoint != 'login' and request.endpoint != 'index' and request.endpoint != 'handle_authorize' and request.endpoint != 'authorized' and request.endpoint != 'clear_token':
        if 'access_token' not in session:
            return redirect(url_for('login'))

@app.route('/')
def index():
    if 'access_token' in session:
        print(session['access_token'])
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')


@app.context_processor
def utility_functions():
    def print_in_console(message):
        print(str(message))

    return dict(mdebug=print_in_console)

@app.route('/create-project', methods=['GET', 'POST'])
def create_project(title="", desc="", location=""):
    project = Project(title, desc, system().get_n_projects())
    project.set_location(location)
    currency_result = get_currencies()
    skills_result = get_skills()
    if (request.method == "POST"):
        title = request.form['title']
        desc = request.form['description']
        location = request.form['location']
        print(request.form)
        i = 1
        # Populate jobs for the project.
        for i in range(1, int(request.form['nJobs']) + 1):
            print(str(i) + " of " + str(request.form['nJobs']) + "!\n")
            print("i: " + str(i) + ", len: " + str(len(request.form)) + "\n")
            num_string = str(i)
            role = request.form[num_string + "-role"]
            job_desc = request.form[num_string + "-description"]
            budget_min = float(request.form[num_string + "-budget-min"])
            budget_max= float(request.form[num_string + "-budget-max"])
            curr = request.form[num_string + "-currency"]
            skills = request.form[num_string + "-hidden-skills"]
            curr_id = get_curr_id(curr, currency_result)
            skill_list = skills.split("|")
            skill_list = skill_list[1:]
            skill_id_list = []
            for skill in skill_list:
                entry = {"id": get_skill_id(skill, skills_result)}
                skill_id_list.append(entry)
            new_job = Job(i, role, job_desc, budget_min, budget_max, curr_id, skill_id_list)
            new_job.set_skills(skill_id_list)
            new_job.set_skill_names(skill_list)
            response = post_job(new_job)
            new_job.set_job_id(response['result']['id'])
            new_job.set_job_link(response['result']['seo_url'])
            project.add_job(new_job)
            i += 1
        project.set_title(title)
        project.set_desc(desc)
        system().add_project(project)
        return redirect(url_for("dashboard"))

    currencies = []
    skill_names = []
    n_jobs = 0
    id = request.args.get('id')
    if (id is not None):
        project = system().find_package(id)
        print(project)
    else:
        project.set_location(location)
        # system().add_project(project)
    for currency in currency_result['currencies']:
        currencies.append(currency['code'])

    for skill in skills_result:
        skill_names.append(skill['name'])
    return render_template('create_project.html', project=project, jobs = project.get_jobs(), currencies=currencies, skills=skill_names, njobs = n_jobs)

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
    response = response.json()

    session["access_token"] = (response["access_token"])
    session["refresh_token"] = (response["refresh_token"])
    return redirect(url_for("dashboard"))

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
    return render_template('dashboard.html', projects = system().get_projects())

@app.route('/packages')
def packages():
    return render_template('packages.html')

@app.route('/projects/<id>')
def singleProject(id):
    project = system().find_project(id)
    print(project)
    return render_template('individualProject.html', id=id, project=project)
