import sys
from collections import Counter
import json

def get_hashtags(Tweet):
    entities = Tweet.get('entities', {})
    hashtags = entities.get('hashtags', {})
    return [tag['text'].lower() for tag in hashtags]

if __name__ == '__main__':
    fname = "Twitter_data_userlevel.jsonl"
    with open(fname, "r") as fi:
        hash = Counter() # Counter container helps us keep count of how many times equivalent values are added
        for line in fi:
            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            hash.update(hashtags_in_tweet)
        for tag,count in hash.most_common(20):
            print("{}:{}".format(tag, count))

