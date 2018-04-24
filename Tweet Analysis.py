import sys
from collections import defaultdict
import json

def get_hashtags(tweet):
    entities = tweet.get('entities',{})
    hashtag = entities.get('hashtags',{})
    return [tag['text'].lower() for tag in hashtag]

if __name__ == '__main__':
    fname = "Twitter_data_userlevel.jsonl"
    with open(fname,"r") as fi:
        hashtag_count = defaultdict(int)
        for line in fi:
            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            no_of_hashtags = len(hashtags_in_tweet)
            hashtag_count[no_of_hashtags] +=1
        tweets_with_hashtags = sum([count for no_of_tags, count in hashtag_count.items() if no_of_tags > 0 ])
        tweets_no_hashtags = hashtag_count[0]
        tweets_total = tweets_no_hashtags + tweets_no_hashtags
        tweets_with_hashtagshtag_percent = "%.2f" %(tweets_with_hashtags/tweets_total * 100)
        tweets_with_no_hashtag_percent = "%.2f" % (tweets_no_hashtags / tweets_total * 100)

        print("\n {} tweets without hashtags ({}%)".format(tweets_no_hashtags,tweets_with_no_hashtag_percent))
        print("{} tweets with at least one hashtags ({}%) \n".format(tweets_with_hashtags, tweets_with_hashtagshtag_percent))

        for tag_count, tweet_count in hashtag_count.items():
            if tag_count>0:
                percent_total = "%.2f" %(tweet_count/tweets_total*100)
                percent_with_hash = "%.2f" %(tweet_count/tweets_with_hashtags * 100)
                print("{} tweets with {} hashtags ({}% total, {}% with hashtags)".format(tweet_count,tag_count,percent_total,percent_with_hash))