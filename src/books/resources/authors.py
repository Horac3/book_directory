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
from src.books.schemas.schema import AuthorSchema, BookSchema


blp = Blueprint("Authors", "author", description="Author Endpoints")

@blp.route("/author")
class Author(MethodView):
    """
    Author class is a Flask view that handles HTTP requests related to authors.
    It is part of a Flask-Smorest blueprint named "Authors" and provides endpoints for retrieving author data.
    """

    @blp.response(200, AuthorSchema(many=True))
    def get(self):
        """
        Handles the GET request for retrieving all authors.
        Returns a list of all AuthorModel instances in the database.
        """
        return AuthorModel.query.all()