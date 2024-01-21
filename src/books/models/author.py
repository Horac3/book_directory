from db import db


class AuthorModel(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(255), unique=False, nullable=False)
    books = db.relationship(
        "BookModel", back_populates="author", lazy="dynamic", cascade="all, delete"
    )

    def __init__(self, author_name):
        self.author_name = author_name
