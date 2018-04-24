import sys
from collections import Counter
import json

def get_mentions(Tweet):
    entities = Tweet.get('entities', {})
    mentions = entities.get('user_mentions', {})
    return [tag['name'].lower() for tag in mentions]

if __name__ == '__main__':
    fname = "Twitter_data_userlevel.jsonl"
    with open(fname, "r") as fi:
        hash = Counter() # Counter container helps us keep count of how many times equivalent values are added
        hash.clear()
        for line in fi:
            tweet = json.loads(line)
            mentions_in_tweet = get_mentions(tweet)
            hash.update(mentions_in_tweet)
        for tag, count in hash.most_common(20):
            print("{}:{}".format(tag, count))
