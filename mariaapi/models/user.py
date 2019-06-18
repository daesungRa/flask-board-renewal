from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True)
    username = Column(String(50), nullable=False)
    pwd = Column(String(200), nullable=False)
    nickname = Column(String(50), unique=True, nullable=False)
    profile = Column(String(200), nullable=False, default='blank_profile01.png')
    auth = Column(Integer, nullable=False, default=1)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, pwd, username, nickname, profile=None):
        self.email = email
        self.username = username
        self.pwd = pwd
        self.nickname = nickname
        self.profile = profile
        self.auth = 1
        self.created = str(datetime.utcnow()).split('.')[0]

    def __repr__(self):
        return f'User("{self.email}", "{self.username}", "{self.nickname}", "{self.profile}")'

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}