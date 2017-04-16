#!/usr/bin/python
import tweepy
import csv
import argparse
import os

consumer_key = "SUAn5eS9GsAD3lLSDdyPp8Hc0"
consumer_secret = "8U0ljImrgvZDMdYgI2RbZF1WXcDPsgb16YN1fmQIKSqwkafp0s"

access_token = "1428703016-TalfNOsCLbsxkGXqVxp2nsnrdipYZkmR8OHYeAk"
access_token_secret = "ZzTyCTEQhlzMDWAdumdU2hlYfnMZx2yrHsj26x10PrlYr"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

dir_path = os.path.dirname(__file__)

def twitterApi(screen_name):
    maxTweets = 2000  # Some arbitrary large number
    tweetsPerQry = 200  # this is the max the API permits

    tweets = []
    tweetCount = 0
    print("Search:" + screen_name)
    print("Downloading max {0} tweets".format(maxTweets))

    new_tweets = api.user_timeline(screen_name = screen_name,count=tweetsPerQry)
    tweetCount += len(new_tweets)
    tweets.extend(new_tweets)

    oldest_tweet = tweets[-1].id -1

    while (tweetCount < maxTweets) and (len(new_tweets) > 0):
        try:
            new_tweets = api.user_timeline(screen_name = screen_name,count=tweetsPerQry,max_id=oldest_tweet)
            tweets.extend(new_tweets)

            tweetCount += len(new_tweets)
            if (maxTweets - tweetCount <= tweetsPerQry):
                tweetsPerQry = maxTweets -tweetCount
            print("Downloaded {0} tweets".format(tweetCount))
            oldest_tweet = tweets[-1].id -1

        except tweepy.TweepError as e:
            #  Exit if any error
            print("some error : " + str(e))
            break

    outtweets = [[tweet.text.encode('unicode_escape')] for tweet in tweets]

    rel_path = 'tweets/%s_tweets.csv' % screen_name
    path = os.path.join(dir_path,rel_path)
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)
        
    print("Downloaded {0} tweets".format(tweetCount))

    pass

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='Process the twitter Name')
    ap.add_argument('name', help='Name of Twitter user', nargs='?', default="nostring")
    args = ap.parse_args()
    if(args.name != "nostring"):
        twitterApi(args.name)