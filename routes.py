from flask import render_template, request, redirect, url_for, abort
from server import app
from models.Project import Project
from models.Job import Job

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-project', methods=['GET', 'POST'])
def create_project(title="", desc="", location=""):
    if (request.method == "POST"):
        title = request.form['title']
        desc = request.form['description']
        location = request.form['location']

    project = Project(title, desc)
    project.set_location(location)
    print(type(project.get_jobs))
    #print(len(project.get_jobs))

    return render_template('create_project.html', jobs = project.get_jobs)