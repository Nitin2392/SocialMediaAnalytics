import json
from tweepy import Cursor
from TwitterMining import get_twitter_client

if __name__ == '__main__':
    client = get_twitter_client()

    for status in Cursor(client.home_timeline).items(20):
        print(status.text) #prints latest 20 tweets/ retweets        )

    for page in Cursor(client.home_timeline, count=200).pages(4):
        for status in page:
            file = open("Twitter_data.jsonl", "w")
            file.write(json.dumps(status._json) + "\n")
            file.close()