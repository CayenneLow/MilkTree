from flask import render_template, request, redirect, url_for, abort
from server import app
from models.Project import Project
from models.Job import Job

def system():
    return app.config['SYSTEM']

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