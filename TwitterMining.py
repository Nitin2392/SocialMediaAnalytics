# Trying to mine data about ICO's from Twitter
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Personalized access tokens for obtaining data from Twitter
access_token = "2606854082-5nqGfM0ywkbzxdrUM0FzepkgmBqNaLuBc8CZQXJ"
access_token_secret = "yVSDaGz4b2Y8bZ03eiEVJWKVmBnvriXqVfdQ4meptoEJ1"
consumer_key = "LPm15qCSlAKvVbCefyucvoIa5"
consumer_secret = "en8SmXnin790nH345cYdkdIu19C8XaZ3P4dcM8j42yDeuEUcYn"

class StdOutListener(StreamListener):

    def on_data(self,data):
        # Write to file
        file = open("Twitter_data.txt","w")
        file.write(data)
        file.close()
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == '__main__':

    #Handle connection to Twitter streaming API
    mom = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth, mom)

    stream.filter(track = ['ICO'])

