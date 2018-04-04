import json
import pandas as pd
import matplotlib.pyplot as plt

read_twitter_data = 'C:/Users/Nitin Rangarajan/PycharmProjects/SocialMediaAnalytics/Twitter_data.txt'

tweets_data = []
tweets_file = open(read_twitter_data, "r")
for line in tweets_file:
    try:
        tweets = json.loads(line)
        tweets_data.append(tweets)
    except:
        continue

print("Here")
print(tweets_data)