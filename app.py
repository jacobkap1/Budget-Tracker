from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, flash, session
from flask_session import Session
from helpers import *
import time
import json

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

session_permanent_state = False
app.config['SESSION_PERMANENT'] = session_permanent_state
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MESSAGE_FLASHING_OPTIONS'] = {'duration': 5}
Session(app)

db = SQL("sqlite:///database.db")

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = 0
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route('/', methods = ['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')