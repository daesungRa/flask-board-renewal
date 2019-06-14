import os
from secrets import token_hex
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
secret_key = token_hex(16)
session_config = {
    "permanent_session_lifetime": timedelta(minutes=60)
}
db_config = {
    "mongodb": {
        "url": "mongodb://localhost:27017/",
        "maxPoolSize": 100,
        "name": "flaskdb",
        "user": "tester",
        "password": "tester"
    },
    "mariadb": {
        "host": "localhost",
        "port": 3306,
        "user": "flask_user",
        "passwd": "0000",
        "db": "flaskdb",
        "charset": "utf8",
        "autocommit": True
    },
    "sqlalchemy": {
        "database_uri": 'mysql+pymysql://flask_user:0000@localhost/flaskdb',
        "track_modifications": False
    }
}