from flask import Flask
from .db_model import DB, User

app = Flask(__name__)

def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\jerem\\Github\\TwitOff\\twitoff.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    @app.route('/<username>/<followers>')
    def add_user(username, followers):
        user = User(username=username, followers=followers)
        DB.session.add(user)
        DB.session.commit()

        return f'{username} has been added to the DB!'

    @app.route('/<username>//<tweet>')
    def add_tweet(username, tweet):
        user = User(username=username, tweet=tweet)
        DB.session.add(tweet)
        DB.session.commit()

        return f'{username}s tweet has been added to the DB!'

    return app