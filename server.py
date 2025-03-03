from linecache import clearcache
from flask import Flask, request, jsonify, make_response, Blueprint
import json
from dotenv import load_dotenv, dotenv_values
import routers.routerAccounts as routers
import os
from config.configMail import ConfigMail
from extension import mail
from models.modelsORM import db
import pymysql
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail

pymysql.install_as_MySQLdb()


load_dotenv(override=True)

env = os.getenv



def create_app(config_name=None):
    app = Flask(__name__)
    print(f"estas en: {config_name}")
    app.config["CACHE_TYPE"] = "simple"

    app.register_blueprint(routers.accountManager)
    app.register_blueprint(routers.forgotAccountManager)
    app.register_blueprint(routers.authTokenManager)

    # Configuración de CORS para permitir el acceso desde cualquier origen
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    app.config.update(vars(ConfigMail))

    mail = Mail(app)
    if config_name != "production":
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f'mysql://{env("USER_DB")}:{env("PASSWORD_DB")}@{env("HOST_DB")}/{env("TESTING_DB")}'
        )
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f'mysql://{env("USER_DB")}:{env("PASSWORD_DB")}@{env("HOST_DB")}/{env("DATABASE_DB")}'
        )
    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        if config_name != "production":
            db.drop_all()
        db.create_all()

    mail.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app("production")
    app.run(debug=True)
    mail.init_app(app)
