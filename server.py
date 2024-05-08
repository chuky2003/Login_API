from flask import Flask, request, jsonify, make_response, Blueprint
from utils.queryManager import queryInsert, queryGetRows
import json
import bcrypt
from dotenv import load_dotenv, dotenv_values
import routers.routerAccounts as routers
import os
from flask_mail import Mail, Message
from config.configMail import ConfigMail
from extension import mail
from flask_sqlalchemy import SQLAlchemy
from models.modelsORM import db
import pymysql
from sqlalchemy import create_engine,text
from flask_migrate import Migrate
from flask_cors import CORS
import asyncio
#from flask_caching import Cache


pymysql.install_as_MySQLdb()

load_dotenv()

env = os.getenv

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
#cache = Cache(app)


# Registrando las rutas definidas en routersAccounts.py
app.register_blueprint(routers.accountManager)
app.register_blueprint(routers.forgotAccountManager)

# Configura CORS para permitir el acceso desde cualquier origen
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['MAIL_SERVER'] = ConfigMail.MAIL_SERVER
app.config['MAIL_PORT'] = ConfigMail.MAIL_PORT
app.config['MAIL_USE_SSL'] = ConfigMail.MAIL_USE_SSL
app.config['MAIL_USE_TLS'] = ConfigMail.MAIL_USE_TLS
app.config['MAIL_USERNAME'] = ConfigMail.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = ConfigMail.MAIL_PASSWORD
app.config["MAIL_DEFAULT_SENDER"]=ConfigMail.MAIL_USERNAME
    

mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{env("USER_DB")}:{env("PASSWORD_DB")}@{env("HOST_DB")}/{env("DATABASE_DB")}'
#print(app.config['SQLALCHEMY_DATABASE_URI'])
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:195418@127.0.0.1/zeroForum'
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

if (__name__ == '__main__'):
    app.run(debug=True)
    mail.init_app(app)