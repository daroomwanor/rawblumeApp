import os
from rawblumeApp import db

class UsersTable(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(120), unique=False, nullable=False)
	lastname = db.Column(db.String(120), unique=False, nullable=False)
	username = db.Column(db.String(120), unique=True, nullable=True)
	email = db.Column(db.String(120), unique=False, nullable=False)
	password = db.Column(db.String(250), unique=False, nullable=True)


class appSettingsTable(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), unique=True, nullable=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	role = db.Column(db.String(120), unique=False, nullable=False)

	
		