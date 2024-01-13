from db import db

class PublisherModel(db.Model):
    __tablename__ = "publishers"
    
    id = db.Column(db.integer, primary_key = True, autoincrement = True)
    publisher_name = db.Column(db.String(255), unique = False, nullable = False)
    
    books = db.relationship(
        "BookModel", back_populates="publishers", lazy="dynamic", cascade="all, delete"
    )