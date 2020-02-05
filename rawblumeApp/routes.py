import os
import time
from flask import render_template, request
from rawblumeApp import app

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/Admin_Panel")
def Admin_Panel():
    return render_template('Admin_Panel.html')