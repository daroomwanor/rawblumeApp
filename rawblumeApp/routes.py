import os
import time
from flask import render_template, request
from rawblumeApp import app, db
from rawblumeApp.models import UsersTable, InventoryTable
import json

@app.route("/", methods=['GET', 'POST'])
def index():
	Users = UsersTable.query.with_entities(UsersTable.firstname).all()
	return render_template('index.html')


@app.route("/Admin_Panel", methods=['GET', 'POST'])
def Admin_Panel():
	Users = UsersTable.query.with_entities(UsersTable.firstname).all()
	return render_template('Admin_Panel.html', data=Users)

@app.route("/getInventoryList", methods=['GET', 'POST'])
def getInventoryList():
	Items = InventoryTable.query.with_entities(InventoryTable.id, InventoryTable.name, InventoryTable.price, InventoryTable.category, InventoryTable.item_id,
		InventoryTable.unit, InventoryTable.description).all()
	data =[]
	for item in Items:
		data.append([item[0],item[1],item[2],item[3],item[4],item[5],item[6].decode('utf-8')])
	return render_template('inventory.html', data = data)

@app.route("/getInventory", methods=['GET', 'POST'])
def getInventory():
	data = json.loads(request.data)
	res = []
	Items = InventoryTable.query.filter(InventoryTable.id == data['id']).with_entities(InventoryTable.id, InventoryTable.name, InventoryTable.price, InventoryTable.category, InventoryTable.item_id,
		InventoryTable.unit,InventoryTable.description).all()
	data =[]
	for item in Items:
		data.append([item[0],item[1],item[2],item[3],item[4],item[5],item[6].decode('utf-8')])
	resp = {
	'data': data
	}
	return resp
@app.route("/updateInventory", methods=['GET', 'POST'])
def updateInventory():
	data = json.loads(request.data)
	item = InventoryTable.query.filter(InventoryTable.id == data['pid']).one()
	if item:
		item.name = data['name']
		item.price = data['price']
		item.category = data['type']
		item.item_id = data['item_id']
		item.unit = data['unit']
		item.description = data['descp'].encode('utf-8')
		db.session.commit()
		return "Success"
	else:
		return "Failed"

@app.route("/deleteInventory", methods=['GET', 'POST'])
def deleteInventory():
	data = json.loads(request.data)
	Item = InventoryTable.query.filter(InventoryTable.id == data['id']).one()
	db.session.delete(Item)
	db.session.commit()
	return "Success"


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
			description = data['descp'].encode('utf-8'))
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
