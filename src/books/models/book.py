

from db import db


class BookModel(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.integer, primary_key = True, autoincrement = True)
    book_name = db.Column(db.String(255), unique = False, nullable = False)
    author_id = db.Column(db.integer, db.ForeignKey("authors.id"), unique = False, nullable = False)
    publisher_id = db.Column(db.integer, db.ForeignKey("publishers.id"), unique = False, nullable = False)
    publication_date = db.Column(db.String(255))
    year = db.Column(db.DateTime)
    isbn = db.Column(db.Interger, unique=True, nullable=False)
    
    author = db.relationship("AuthorModel", back_populates="books")
    publisher = db.relationship("PublisherModel", back_populates="books")