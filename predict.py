from sklearn.linear_model import LogisticRegressionCV
import numpy as np
from .models import User
from .twitter import vectorize_tweet


def predict_user(user0_username, user1_username, hypo_tweet_text):

    # Grab the users from the DB
    user0 = User.query.filter(User.username == user0_username).one()
    user1 = User.query.filter(User.username == user1_username).one()

    # Get the work embeddings from each user
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    # vertically stack
    vects = np.vstack([user0_vects, user1_vects])

    # concatenate our labels of 0 or 1 for each tweet
    zeros = np.zeros(len(user0.tweets))
    ones = np.ones(len(user1.tweets))

    labels = np.concatenate([zeros, ones])

    # Instantiate and fit a logistic regression model
    log_reg = LogisticRegression()

    # train our logistic regression
    log_reg.fit(vects, labels)

    # vectorize (get the word embeddings for)
    #  our hypothetical tweet text
    hypo_tweet_text = vectorize_tweet(hypo_tweet_text)

    # get a prediction for which user is more likely to say the hypo_tweet_text
    prediction = log_reg.predict(hypo_tweet_text.reshape(1, -1))

    print(prediction)
