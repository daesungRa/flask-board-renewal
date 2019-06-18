from flask import Flask, logging
from flask_cors import CORS
from flask_bcrypt import Bcrypt

import config
from mariaapi.models import user

# SQLAlchemy model & bcrypt object
db = user.db
flask_bcrypt = Bcrypt()

def create_app():
    """[main.create_app]: flask application 생성 및 환경설정 후 반환하는 모듈입니다. SQLAlchemy,
    CORS, logging, flask_bcrypt 패키지가 포함됩니다."""

    app = Flask(__name__, static_folder='static', static_url_path='')
    app.config['SECRET_KEY'] = config.secret_key
    app.config['PERMANENT_SESSION_LIFETIME'] = config.session_config['permanent_session_lifetime']
    app.config['SQLALCHEMY_DATABASE_URI'] = config.db_config['sqlalchemy']['database_uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.db_config['sqlalchemy']['track_modifications']
    db.init_app(app)
    CORS(app)
    logging.create_logger(app)
    flask_bcrypt.init_app(app)

    return app



