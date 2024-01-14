from dbm import dumb
from marshmallow import Schema, fields
from sqlalchemy import false

class PlainBookSchema(Schema):
    id = fields.Int(dump_only=True)
    book_name = fields.Str(required=True)
    publication_date = fields.Str(required=False)
    isbn = fields.Str(required=False)
    
class PlainAuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    author_name = fields.Str(required=True)
    
class PlainPublisherSchema(Schema):
    id = fields.Int(dump_only=True)
    publisher_name = fields.Str(required=True)
    

class BookSchema(PlainBookSchema):
    author_name = fields.Str(required=False, load_only=True)
    publisher_name = fields.Str(required=False, load_only=True)
    author = fields.Nested(PlainAuthorSchema(), dump_only = True)
    publisher = fields.Nested(PlainPublisherSchema(), dump_only=True)
    

class AuthorSchema(PlainAuthorSchema):
    books = fields.List(fields.Nested(PlainBookSchema()), dump_only=True)
    

class PublisherSchema(PlainPublisherSchema):
    books = fields.List(fields.Nested(PlainBookSchema()), dump_only=True)
