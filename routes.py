from flask import render_template, request, redirect, url_for, abort
from server import app
from models.Project import Project

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-project', methods=['GET', 'POST'])
def create_project():
    if request.method != "POST":
        return 
    
    title = request.form['title']
    desc = request.form['desc']
    location = request.form['location']

    project = Project(title, desc)
    project.set_location(location)

    return render_template('create-project.html')


