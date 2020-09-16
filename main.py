import tweepy
import requests
import datetime
from random import randint
from time import sleep
from Confidential import *

URL = "https://api.kanye.rest/"

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__(api)

    def on_status(self, status):
        if "@DavenBot" in status.text and "#kanye" in status.text \
                and status.author.screen_name != "DavenBot":
            result = run(api, status)


def get_twitter_api():
    """
    Returns Twitter API.
    :return:
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth, wait_on_rate_limit=True)


def get_kanye_quote():
    r = requests.get(URL)
    json = r.json()
    print("Posting Quote... " + " " + json["quote"])
    return json['quote']


def run(api: tweepy.API, tweet=None):
    """
    Initialize our twitter bot.
    """
    print("Getting Kanye Quote")
    quote = get_kanye_quote()

    output_tweet = quote + " -Kanye West"
    if tweet is not None:
        output_tweet = "@%s %s" % (tweet.author.screen_name, output_tweet)
        result = api.update_status(status=output_tweet,
                                   in_reply_to_status_id=tweet.id)
    else:
        result = api.update_status(status=output_tweet)
    print("Posted to Twitter")
    return result


if __name__ == '__main__':
    print("Getting Twitter API")
    api = get_twitter_api()
    myStreamListener = MyStreamListener(api)
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["@DavenBot", "#kanye", "@davenbot"], is_async=True)

    while True: # Infinite loop so a mention to bot isn't required to tweet
        run(api)
        random_int = randint(3600, 21600) # tweets randomly between 1 - 6 hrs
        time = datetime.timedelta(seconds=random_int)
        print("Waiting for " + str(time))
        sleep(random_int)



