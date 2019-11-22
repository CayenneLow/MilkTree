from flask import render_template, request, redirect, url_for, abort
from server import app
#from models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-project', methods=["GET", "POST"])
def create_project():
    return render_template('create_project.html')
