import json
from tweepy import Cursor
# This refers to the TwitterMining file in the same library
from TwitterMining import get_twitter_client

if __name__ == '__main__':
    # AuctusProject is a company that just completed ICO campaign
    user = "AuctusProject"
    # Call get_twtter_client method of TwitterMining.Py
    client = get_twitter_client()
    
    # Run through user timeline to fetch latest 20 Tweets and print them
    for status in Cursor(client.user_timeline).items(20):
        print(status.text)

    # Search API allows us to retreive 3200 tweets of information for a period of 10 minutes.
    # JSON data is fetched from Twitter and stored in the said file in jsonl format
    for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
        for status in page:
            file = open("Twitter_data_userlevel.jsonl", "a")
            file.write(json.dumps(status._json) + "\n")
            file.close()
