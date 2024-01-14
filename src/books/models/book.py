

from db import db


class BookModel(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    book_name = db.Column(db.String(255), unique = False, nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    publication_date = db.Column(db.String(255))
    isbn = db.Column(db.String(255), unique = False)
    author = db.relationship("AuthorModel", back_populates="books")
    publisher = db.relationship("PublisherModel", back_populates="books")