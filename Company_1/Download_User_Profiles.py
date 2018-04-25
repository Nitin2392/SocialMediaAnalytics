import os
import sys
import json
import time
import math
from tweepy import Cursor
from Company_1.TwitterMining import get_twitter_client

MAX_FRIENDS = 15000


def paginate(items, n):
    '''

    :param items:
    :param n:
    :return:
    '''

    for i in range(0, len(items), n):
        yield items[i:i+n]

if __name__ == '__main__':

    screen_name = "effectaix"
    client = get_twitter_client()
    dirname = "users/{}".format(screen_name)
    max_pages = math.ceil(MAX_FRIENDS/5000)
    try:
        os.makedirs(dirname, mode=0o755, exist_ok=True)
    except OSError:
        print("Directory {} already exists".format(dirname))
    except Exception as e:
        print("Error while creating directory {}".format(dirname))
        print(e)
        sys.exit(1)

    # get followers for a user
    fname = "users/{}/followers.jsonl".format(screen_name)
    with open(fname, "w") as fi:
        for followers in Cursor(client.followers_ids, screen_name=screen_name).pages(max_pages):
            for chunk in paginate(followers, 100):
                users = client.lookup_users(user_ids=chunk)
                for user in users:
                    fi.write(json.dumps(user._json)+"\n")
            if len(followers) == 5000:
                print("More results available. Sleeping for 60 seconds to avoid rate limit")
                time.sleep(60)

    fname = "users/{}/friends.jsonl".format(screen_name)
    with open(fname, "w") as fi:
        for friends in Cursor(client.friends_ids, screen_name=screen_name).pages(max_pages):
            for chunk in paginate(friends, 100):
                users = client.lookup_users(user_ids=chunk)
                for user in users:
                    fi.write(json.dumps(user._json) + "\n")
            if len(friends) == 5000:
                print("More results available. Sleeping for 60 seconds to avoid rate limit")
                time.sleep(60)

    fname = "users/{}/user_profile_json".format(screen_name)
    with open(fname, "w") as fi:
        profile = client.get_user(screen_name=screen_name)
        fi.write(json.dumps(profile._json, indent=4))
