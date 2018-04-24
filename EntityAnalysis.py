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
        hash_new = Counter() # Counter container helps us keep count of how many times equivalent values are added
        hash_new.clear()
        for line in fi:
            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            hash_new.update(hashtags_in_tweet)
        for tag,count in hash_new.most_common(100):
            print("{}:{}".format(tag, count))

