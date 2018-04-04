import json
from tweepy import Cursor
from TwitterMining import get_twitter_client

if __name__ == '__main__':
    user = "Any Twitter User Handle can go here"
    client = get_twitter_client()

    for status in Cursor(client.home_timeline).items(20):
        print(status.text)

    for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(4):
        for status in page:
            file = open("Twitter_data_userlevel.jsonl", "w")
            file.write(json.dumps(status._json) + "\n")
            file.close()
