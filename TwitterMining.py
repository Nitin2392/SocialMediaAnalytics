# Trying to mine data about ICO's from Twitter
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

# Personalized access tokens for obtaining data from Twitter
def get_twitter_data():
    access_token = "2606854082-5nqGfM0ywkbzxdrUM0FzepkgmBqNaLuBc8CZQXJ"
    access_token_secret = "yVSDaGz4b2Y8bZ03eiEVJWKVmBnvriXqVfdQ4meptoEJ1"
    consumer_key = "LPm15qCSlAKvVbCefyucvoIa5"
    consumer_secret = "en8SmXnin790nH345cYdkdIu19C8XaZ3P4dcM8j42yDeuEUcYn"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_data()
    client = API(auth)
    return client


