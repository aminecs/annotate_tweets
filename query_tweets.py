import tweepy, os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"), os.environ.get("CONSUMER_SECRET"))
auth.set_access_token(os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

obj_ = api.statuses_lookup([665257826961530880,
665257828479860736,
665257828941209600,
665257832170848257,
665257832590278656,
665257833500426241,
665257835144601600,
665257838290292736,
665257840844652544,
665257846020440064,
665257847337443330,
665257848457330689])

with open("sample.ids", "w") as annotated:
    for tweet in obj_:
        print("ID: ", tweet.id_str)
        print("Tweet: ", tweet.text)
        annotation = input("Annotate (0: Not relevant, 1: Relevant, 2: Informative): ")
        if int(annotation) < 0 or int(annotation) > 2:
            raise Exception("Invalid annotation: ", annotation)
        annotated.write(tweet.id_str + "," + annotation + "\n")
