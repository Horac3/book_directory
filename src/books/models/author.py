from db import db

class AuthorModel(db.Model):
    __tablename__ = "authors"
    
    id = db.Column(db.integer, primary_key = True, autoincrement = True)
    author_name = db.Column(db.String(255), unique = False, nullable = False)
    
    books = db.relationship(
        "BookModel", back_populates="authors", lazy="dynamic", cascade="all, delete"
    )