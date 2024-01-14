import imp
import re
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema
from sqlalchemy.exc import SQLAlchemyError

from db import db
from src.books.models import publisher
from src.books.models.author import AuthorModel
from src.books.models.publisher import PublisherModel
from src.books.models.book import BookModel
from src.books.schemas.schema import BookSchema, PublisherSchema

blp = Blueprint("Publisher", "publishers", description = "Publisher Endpoints")

@blp.route("/publisher")
class PlainPublisherSchema(MethodView):
    @blp.response(200, PublisherSchema(many=True))
    def get(self):
        return PublisherModel.query.all()
    
    # @blp.arguments(BookSchema)
    # @blp.response(201, BookSchema(many=True))
    # def post(self, books_data):
    #     books = BookModel(**books_data)
        
    #     if books.author_name or books.publisher_name:
    #         print(f"Author name {books.author_name} Book Publisher {books.publisher_name}")
    #         author = AuthorModel(author_name=books.author_name)
    #         publisher = PublisherModel(publisher_name=books.publisher_name)
    #         db.session.add(author)
    #         db.session.add(publisher)
    #     db.session.add(books)
    #     db.session.commit()
    #     return BookModel.query.all()