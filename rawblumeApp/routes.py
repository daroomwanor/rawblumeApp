import os
import time
from flask import render_template, request
from rawblumeApp import app, db
from rawblumeApp.models import UsersTable

@app.route("/")
def index():
	Users = UsersTable.query.with_entities(UsersTable.firstname).all()
	return render_template('index.html', data=Users)


@app.route("/Admin_Panel")
def Admin_Panel():
    return render_template('Admin_Panel.html')



@app.route("/processLogin")
def processLogin():
	users = UsersTable(
		firstname="Admin",
		lastname="Root",
		email="admin@root.com",
		username="Admin",
		password="pass")
	db.session.add(users)
	db.session.commit()
	return "Successful"
