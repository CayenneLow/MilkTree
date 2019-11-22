from flask import Flask
from System import System

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy