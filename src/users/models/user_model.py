from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    role = db.Column(db.String())
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
