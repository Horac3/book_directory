from db import db

class PublisherModel(db.Model):
    __tablename__ = "publishers"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    publisher_name = db.Column(db.String(255), unique = False, nullable = True)
    
    books = db.relationship(
        "BookModel", back_populates="publisher", lazy="dynamic", cascade="all, delete"
    )
    
    def __init__(self, publisher_name):
        self.publisher_name = publisher_name
        