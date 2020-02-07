import os
import time
from flask import render_template, request
from rawblumeApp import app, db
from rawblumeApp.models import UsersTable
import json

@app.route("/")
def index():
	Users = UsersTable.query.with_entities(UsersTable.firstname).all()
	return render_template('index.html', data=Users)


@app.route("/Admin_Panel")
def Admin_Panel():
	Users = UsersTable.query.with_entities(UsersTable.firstname).all()
	return render_template('Admin_Panel.html',data=Users)



@app.route("/processLogin")
def processLogin():
	data = json.loads(request.data)
	print(data)
	username = data['username']
	password = data['password']
	User = UsersTable.query.filter_by(UsersTable.username == username).all()
	if len(User) > 0:
		print(username)
		return "Success"


@app.route("/processLogin")
def addNewUser():
	users = UsersTable(
		firstname="Admin",
		lastname="Root",
		email="admin@root.com",
		username="Admin",
		password="pass")
	db.session.add(users)
	db.session.commit()
	return "Successful"
