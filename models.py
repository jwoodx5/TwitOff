from flask_sqlalchemy import SQLAlchemy

# create a DB object from the SQLAlchemy class

DB = SQLAlchemy()


class User(DB.Model):
# id column
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
# username column
    username = DB.Column(DB.String, nullable=False)
    # backref is as=if we had added a tweets list to the user class
    # tweets = []

    # def __repr__(self):
    #     return f"User: {self.username}"

class Tweet(DB.Model):
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    # text column   
    text = DB.Column(DB.Unicode(300), nullable=False)
    # Create a relationship between Users and Tweets
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    # Create a whole list of tweets to be attached to the User
    user = DB.relationship('User', backref=DB.backref('tweets'), lazy=True)

    # def __repr__(self):
    #     return f"Tweet: {self.text}"

