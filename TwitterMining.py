# Trying to mine data about ICO's from Twitter

# Tweepy will be primary library/package we will be using to connect to Twitter
from tweepy.streaming import StreamListener
# Need this to authentcate OAuthHandler which will be used for Authenticating User profiles
from tweepy import OAuthHandler
# In Case of streaming API 
from tweepy import Stream
# To invoke Twitter API 
from tweepy import API

# Personalized access tokens for obtaining data from Twitter
def get_twitter_data():
    # I have not specified any tokens here. Create a Twitter application and once the ID's are generated, substitute them here. 
    access_token = "Your Access Token goes here"
    access_token_secret = "Your Access Token Secret goes here"
    consumer_key = "Your Consumer Key goes here"
    consumer_secret = "Your Comsumer Secret goes here"
    # Using OAuthHandler method and passing consumer key and secret followed by setting access token and secret
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_data()
    # Fetch Search API after user authentication
    client = API(auth)
    return client


