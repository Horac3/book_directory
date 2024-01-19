

from db import db


class BookModel(db.Model):
    """
    Represents a model for books in a database.
    Defines the structure and relationships of the book data.
    """

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    publisher_id = db.Column(db.Integer, db.ForeignKey("publishers.id"))
    author_name = db.Column(db.String(255), nullable=True)
    publisher_name = db.Column(db.String(255), nullable=True)
    publication_date = db.Column(db.String(255))
    isbn = db.Column(db.String(255))

    author = db.relationship("AuthorModel", back_populates="books")
    publisher = db.relationship("PublisherModel", back_populates="books")

    def __repr__(self):
        return f"<BookModel(book_name='{self.book_name}', author_id={self.author_id}, publisher_id={self.publisher_id}, publication_date='{self.publication_date}', isbn='{self.isbn}')>"

    def __init__(self, book_name: str, author_id: int, publisher_id: int, publication_date: str, isbn: str):
        """
        Initializes a new instance of the BookModel class.

        Args:
            book_name (str): The name of the book.
            author_id (int): The ID of the associated author.
            publisher_id (int): The ID of the associated publisher.
            publication_date (str): The publication date of the book.
            isbn (str): The ISBN of the book.
        """
        self.book_name = book_name
        self.author_id = author_id
        self.publisher_id = publisher_id
        self.publication_date = publication_date
        self.isbn = isbn