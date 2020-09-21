from flask import Flask, request, render_template
from application import app
import random
import requests

@app.route('/', methods=['GET'])
def get_users():
    response = requests.get('http://35.246.102.140:5001/backend').json()
    return render_template('index.html', title='Home', response=response)
