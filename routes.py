from flask import render_template, request, redirect, url_for, abort
from server import app
from models.Project import Project
from models.Job import Job

@app.route('/')
def index():
    return render_template('index.html')

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
        jobs = []


    project = Project(title, desc)
    project.set_location(location)

    return render_template('create_project.html', jobs = project.get_jobs(), njobs = n_jobs)