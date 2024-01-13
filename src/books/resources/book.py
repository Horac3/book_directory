import imp
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema
from sqlalchemy.exc import SQLAlchemyError

from db import db

from src.books.schemas.schema import BookSchema

blp = Blueprint("Books", "books", description = "Book Endpoints")

@blp.route("/books")
class Book(MethodView):
    @blp.response(200, BookSchema)
    def get(self):
        return "Books"