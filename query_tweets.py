import tweepy, os
from dotenv import load_dotenv
import json

load_dotenv()

def twitter_auth():
    auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), os.environ.get("CONSUMER_SECRET"))
    auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))
    return auth

def get_api(auth):
    api = tweepy.API(auth)
    return api

def lookup_tweets(tweet_ids, api):
    status = api.statuses_lookup(tweet_ids)
    return status

def annotate_tweets(tweet_ids, event_name, start_index, api):
    status = lookup_tweets(tweet_ids, api)
    json_list = []
    with open(event_name + "-" + str(start_index) + ".json", "w") as annotated:
        for tweet in status:
            curr_tweet = {}
            print("ID: ", tweet.id_str)
            print("Tweet: ", tweet.text)
            annotation = input("Annotate (0: Not relevant, 1: Relevant, 2: Informative): ")
            if not annotation or int(annotation) < 0 or int(annotation) > 2:
                annotation = input("Try again: ")
            curr_tweet["annotation"] = annotation
            curr_tweet["tweet_id"] = tweet.id_str
            if hasattr(tweet, "retweeted_status"):
                curr_tweet["text"] = tweet.retweeted_status.text
            else:
                curr_tweet["text"] = tweet.text
            curr_tweet["name"] = tweet.author.name
            curr_tweet["screen_name"] = tweet.author.screen_name
            curr_tweet["profile_img"] = tweet.author.profile_image_url_https
            json_list.append(curr_tweet)
        json.dump(json_list, annotated)
    return True

def main():
    filename = input("Enter filename: ")
    start_index = int(input("Enter start index: "))
    tweet_ids = []
    with open(filename) as event_tweets:
        event_tweets_ids = event_tweets.readlines()
        for i in range(int(start_index), int(start_index)+100):
            tweet_ids.append(int(event_tweets_ids[i]))
    auth = twitter_auth()
    api = get_api(auth)
    annotate_tweets(tweet_ids, filename, start_index, api)

main()