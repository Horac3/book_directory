import imp
import re
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from marshmallow import Schema
from sqlalchemy.exc import SQLAlchemyError

from db import db
from src.books.models import publisher
from src.books.models.author import AuthorModel
from src.books.models.publisher import PublisherModel
from src.books.models.book import BookModel
from src.books.schemas.schema import BookSchema

blp = Blueprint("Books", "books", description = "Book Endpoints")

blp = Blueprint("books", "books", url_prefix="/books")

@blp.route("")
class Book(MethodView):
    @jwt_required()
    @blp.response(200, BookSchema(many=True))
    def get(self):
        """
        Retrieves all books from the database and returns them as a JSON response.
        """
        return BookModel.query.all()
    @jwt_required()
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, book_data):
        """
        Creates a new book based on the provided data. If the author or publisher does not exist in the database, they are created first.
        The created book is then added to the database and returned as a JSON response.
        """
        author_name = book_data.pop("author_name", None)
        publisher_name = book_data.pop("publisher_name", None)
        
        if author_name:
            author = AuthorModel.query.filter_by(author_name=author_name).first()
            print(f"Author {author}")
            if not author:
                author = AuthorModel(author_name=author_name)
                db.session.add(author)
                db.session.commit()
            book_data["author_id"] = author.id
        
        if publisher_name:
            publisher = PublisherModel.query.filter_by(publisher_name=publisher_name).first()
            if not publisher:
                publisher = PublisherModel(publisher_name=publisher_name)
                db.session.add(publisher)
                db.session.commit()
            book_data["publisher_id"] = publisher.id
        
        book = BookModel(**book_data)
        db.session.add(book)
        db.session.commit()
        
        return book