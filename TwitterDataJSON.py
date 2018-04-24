import json
from tweepy import Cursor
from TwitterMining import get_twitter_client

if __name__ == '__main__':
    client = get_twitter_client()
    i=0
    for status in Cursor(client.home_timeline).items(20):
        print(str(i) + " " + status.text)  # prints latest 20 tweets/retweets
        i=i+1

    with open("Twitter_data.jsonl", "w") as write_to_file:
        for page in Cursor(client.home_timeline, count=200).pages(4):
            for status in page:
                write_to_file.write(json.dumps(status._json) + "\n")
