from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    followers = DB.Column(DB.String(120), unique=True, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    tweet = DB.Column(DB.String(500), unique=True, nullable=False)
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, nullable=False, DB.ForeignKey('user.id'))
    user = DB.relationship('User', backref=DB.backref('tweet', lazy=True))

    def __repr__(self):
        return '<Tweet %r>' % self.tweet

# First, to get this to go, go into the flask shell by typing:
# flask shell
# Then, enter: from twitoff.db_model import DB, User, Tweet

# set FLASK_APP=twitoff:APP
# set FLASK_ENV=development
# flask run
