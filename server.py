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


def create_app(production=True):
    app = Flask(__name__)
    app.config["CACHE_TYPE"] = "simple"

    app.register_blueprint(routers.accountManager)
    app.register_blueprint(routers.forgotAccountManager)
    app.register_blueprint(routers.authTokenManager)

    # Configuración de CORS para permitir el acceso desde cualquier origen
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    app.config.update(vars(ConfigMail))

    mail = Mail(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        env("URL_DB") if production else env("URL_DB_TESTING")
    )

    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        if not production:
            db.drop_all()
        db.create_all()

    mail.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app(True)
    app.run(debug=True)
    mail.init_app(app)
