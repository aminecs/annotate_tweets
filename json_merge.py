import json
import os

all_tweets = []
for json_list in os.listdir("json"):
    with open("json/" + json_list) as tweets:
        all_tweets = all_tweets + list(json.load(tweets))

with open("merged_json.json", "w+") as merged_json:
    json.dump(all_tweets, merged_json)