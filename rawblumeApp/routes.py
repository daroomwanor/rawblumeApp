import os
import time
from flask import render_template, request
from rawblumeApp import app, db
from rawblumeApp.models import UsersTable, InventoryTable
import json

@app.route("/", methods=['GET', 'POST'])
def index():
	Users = UsersTable.query.with_entities(UsersTable.firstname).all()
	return render_template('index.html', data=Users)


@app.route("/Admin_Panel", methods=['GET', 'POST'])
def Admin_Panel():
	Users = UsersTable.query.with_entities(UsersTable.firstname).all()
	return render_template('Admin_Panel.html',data=Users)


@app.route("/addNewItem", methods=['GET', 'POST'])
def addNewItem():
	data = json.loads(request.data)
	item = InventoryTable.query.filter(InventoryTable.name == data['name']).all()
	if len(item) < 1:
		Item = InventoryTable(
			name = data['name'],
			price = data['price'],
			category = data['type'],
			item_id= data['item_id'],
			unit = data['unit'],
			description = data['descp'])
		db.session.add(Item)
		db.session.commit()
		return "Success"
	else:
		return "Failed"

@app.route("/processLogin", methods=['GET', 'POST'])
def processLogin():
	data = json.loads(request.data)
	username = data['username']
	password = data['password']
	User = UsersTable.query.filter(UsersTable.username == username, UsersTable.password == password).all()
	if len(User) > 0:
		return "Success"
	else:
		return "Failed"

@app.route("/addNewUser", methods=['GET', 'POST'])
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
