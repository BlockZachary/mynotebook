# -*- coding:utf-8 -*-
# Author: Zachary
import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = os.getenv('MYSQL_PORT', 3306)
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '123456')
MYSQL_DB = os.getenv('MYSQL_DB', 'mynotebook_db')

app = Flask(__name__, template_folder='../templates', static_folder='../static', static_url_path='/static')

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
app.config['SECRET_KEY'] = 'zachary123456'

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from routes import user_routes
from routes import admin_routes
