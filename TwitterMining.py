# Trying to mine data about ICO's from Twitter
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

# Personalized access tokens for obtaining data from Twitter
def get_twitter_data():
    access_token = "Your Access Token goes here"
    access_token_secret = "Your Access Token Secret goes here"
    consumer_key = "Your Consumer Key goes here"
    consumer_secret = "Your Comsumer Secret goes here"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_data()
    client = API(auth)
    return client


