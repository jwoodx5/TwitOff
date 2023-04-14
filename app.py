from flask import Flask, render_template
from .models import DB, User, Tweet


def create_app():

    app = Flask(__name__)

    # database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    # # register our database with the app
    DB.init_app(app)

    # my_var = "Twitoff App"

    @app.route('/')
    def root():

        users = User.query.all()
        # for user in users:
        #     print(user.username)
        #     for tweet in user.tweets:
        #         print(tweet.text)
        return render_template('base.html', title='Home', users=users)

    @app.route('/bananas')
    def bananas():
        print('banana')
        return render_template('base.html', title='Bananas')

    @app.route('/reset')
    def reset():
        # # Drop all database tables
        DB.drop_all()
        # # Recreate all database tables according to the
        # # indicated schema in models.py
        DB.create_all()
        return "database has been reset"

    # @app.route('/update')
    # def populate():

        # create two fake users in the DB
        jamie = User(id=1, username='jamie')
        DB.session.add(jamie)
        john = User(id=2, username='john')
        DB.session.add(john)

        # Create six fake tweets in DB
        tweet1 = Tweet(id=1, text="jamie's first tweet text", user=jamie)
        DB.session.add(tweet1)
        tweet2 = Tweet(id=2, text="john's first tweet text", user=john)
        DB.session.add(tweet2)
        tweet3 = Tweet(id=3, text="jamie's second tweet text", user=jamie)
        DB.session.add(tweet3)
        tweet4 = Tweet(id=4, text="john's second tweet text", user=john)
        DB.session.add(tweet4)
        tweet5 = Tweet(id=5, text="jamie's third tweet text", user=jamie)
        DB.session.add(tweet5)
        tweet6 = Tweet(id=6, text="john's third tweet text", user=john)
        DB.session.add(tweet6)

        # Save the changes we just made to the DB
        # "commit" the DB changes
        DB.session.commit()

        return render_template('base.html', title='Reset')

    return app
