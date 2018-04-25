import sys
import json

if __name__ == '__main__':

    comp1 = "AuctusProject"
    comp2 = "effectaix"

    followers_comp1 = "Company_1/users/{}/followers.jsonl".format(comp1)
    followers_comp2 = "Company_1/users/{}/followers.jsonl".format(comp2)

    with open(followers_comp1, "r") as f1, open(followers_comp2, "r") as f2:
        reach1 = []
        reach2 = []
        for line in f1:
            profile = json.loads(line)
            reach1.append((profile['screen_name'], profile['followers_count']))
        for line in f2:
            profile = json.loads(line)
            reach2.append((profile['screen_name'], profile['followers_count']))

    # Load basic stats

    profile_file1 = "Company_1/users/{}/user_profile_json".format(comp1)
    profile_file2 = "Company_1/users/{}/user_profile_json".format(comp2)

    with open(profile_file1, "r") as f1, open(profile_file2, "r") as f2:
        profile1 = json.load(f1)
        profile2 = json.load(f2)
        followers1 = profile1['followers_count']
        followers2 = profile2['followers_count']
        tweets1 = profile1['statuses_count']
        tweets2 = profile2['statuses_count']

    sum_reach1 = sum([x[1] for x in reach1])
    sum_reach2 = sum([x[1] for x in reach2])
    avg_followers1 = round(sum_reach1 / followers1, 2)
    avg_followers2 = round(sum_reach2 / followers2, 2)

    # Load timelines
    timeline_file1 = "Twitter_data_userlevel.jsonl"
    timeline_file2 = "Twitter_data_userlevel_2.jsonl"

    with open(timeline_file1, "r") as f1, open(timeline_file2, "r") as f2:
        favorited_count1, retweet_count1 = [], []
        favorited_count2, retweet_count2 = [], []
        for line in f1:
            tweet = json.loads(line)
            favorited_count1.append(tweet['favorite_count'])
            retweet_count1.append(tweet['retweet_count'])
        for line in f2:
            tweet = json.loads(line)
            favorited_count2.append(tweet['favorite_count'])
            retweet_count2.append(tweet['retweet_count'])

    # Average number of fav's and retweets

    avg_favorites1 = round(sum(favorited_count1) / tweets1, 2)
    avg_favorites2 = round(sum(favorited_count2) / tweets2, 2)
    avg_retweet1 = round(sum(retweet_count1) / tweets1, 2)
    avg_retweet2 = round(sum(retweet_count2) / tweets2, 2)
    favorited_per_user1 = round(sum(favorited_count1) / followers1, 2)
    favorited_per_user2 = round(sum(favorited_count2) / followers2, 2)
    retweeted_per_user1 = round(sum(retweet_count1) / followers1, 2)
    retweeted_per_user2 = round(sum(retweet_count2) / followers2, 2)

    print("--------- Exploratory Analysis -----------")

    print("Analysis for {}".format(comp1))
    print("{} followers".format(followers1))
    print("{} users reached by 1-degree connections".format(sum_reach1))
    print("Average number of followers for {}'s followers : {}".format(comp1, avg_followers1))
    print("Favorited {} times {} per tweet, {} per user".format(sum(favorited_count1), avg_favorites1, favorited_per_user1))
    print("Retweeted {} times {} per tweet, {} per user".format(sum(retweet_count1), avg_retweet1,
                                                                 retweeted_per_user1))
    print("------------------------------------------")
    print("Analysis for {}".format(comp2))
    print("{} followers".format(followers2))
    print("{} users reached by 1-degree connections".format(sum_reach2))
    print("Average number of followers for {}'s followers : {}".format(comp2, avg_followers2))
    print("Favorited {} times {} per tweet, {} per user".format(sum(favorited_count2), avg_favorites2,
                                                                 favorited_per_user2))
    print("Retweeted {} times {} per tweet, {} per user".format(sum(retweet_count2), avg_retweet2,
                                                                 retweeted_per_user2))



