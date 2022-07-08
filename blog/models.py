from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin

'''
Flask-login requires a User model with the following properties:
    has an is_authenticated() method that returns True if the user has provided valid credentials
    has an is_active() method that returns True if the user’s account is active
    has an is_anonymous() method that returns True if the current user is an anonymous user
    has a get_id() method which, given a User instance, returns the unique ID for that object
UserMixin class provides the implementation of this properties. Its the reason you can call for example is_authenticated to check if login credentials provide is correct or not instead of having to write a method to do that yourself.
'''

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default="default.jpg")
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship("Post", backref="author", lazy=True)         #one to many relationship , one author many posts. lazy argument is to sqlalchemy load the data in one go. Lazy parameter determines how the related objects get loaded when querying through relationships.

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

