import os
from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '4973490d9fdsf-0dr-340-348347850450'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rawblumeApp.db'

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()


import rawblumeApp.routes
from rawblumeApp import models 