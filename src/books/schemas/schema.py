from marshmallow import Schema, fields

class PlainBookSchema(Schema):
    id = fields.Int(dump_only=True)
    book_name = fields.Str(required=True)
    publication_date = fields.Str(required=False)
    isbn = fields.Str(required=False)
    
class PlainAuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    author_name = fields.Str()
    
class PlainPublisherSchema(Schema):
    id = fields.Int(dump_only=True)
    publisher_name = fields.Str()
    

class BookSchema(PlainBookSchema):
    author_id = fields.Int(required=True, load_only=True)
    publisher_id = fields.Int(required=True, load_only=True)
    author = fields.Nested(PlainAuthorSchema(), dump_only=True)
    publisher = fields.Nested(PlainPublisherSchema(), dump_onlt=True)
    

class AuthorSchema(PlainAuthorSchema):
    books = fields.List(fields.Nested(PlainBookSchema()), dump_only=True)
    

class PublisherSchema(PlainPublisherSchema):
    books = fields.List(fields.Nested(PlainBookSchema()), dump_only=True)
