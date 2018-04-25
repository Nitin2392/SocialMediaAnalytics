import sys
import json

def print_details(friends, followers, screenname):
    mutual_friend = [user for user in friends if user in followers]
    followers_not_following = [user for user in followers if user not in friends]
    friends_not_following = [user for user in friends if user not in followers]

    print("{} has {} followers".format(screenname, len(followers)))
    print("{} has {} friends".format(screenname, len(friends)))
    print("{} has {} mutual friends".format(screenname, len(mutual_friend)))
    print("{} friends are not following {} back".format(len(friends_not_following), screenname))
    print("{} followers are not followed back by {}".format(len(followers_not_following), screenname))

if __name__ == '__main__':
    screen_name = "AuctusProject"
    screen_name_2 = "effectaix"
    followers_file = "users/{}/followers.jsonl".format(screen_name)
    friends_file = "users/{}/friends.jsonl".format(screen_name)
    followers_file_two = "users/{}/followers.jsonl".format(screen_name_2)
    friends_file_two = "users/{}/friends.jsonl".format(screen_name_2)
    with open(followers_file, "r") as f1, open(friends_file, "r") as f2:
        followers = []
        friends = []
        for line in f1:
            profile = json.loads(line)
            followers.append(profile['screen_name'])
        for line in f2:
            profile = json.loads(line)
            friends.append(profile['screen_name'])

    with open(followers_file_two, "r") as f1, open(friends_file_two, "r") as f2:
        followers_two = []
        friends_two = []
        for line in f1:
            profile = json.loads(line)
            followers_two.append(profile['screen_name'])
        for line in f2:
            profile = json.loads(line)
            friends_two.append(profile['screen_name'])

    print_details(friends, followers, screenname=screen_name)
    print("--------------------------------------------------")
    print_details(friends_two, followers_two, screenname=screen_name_2)


