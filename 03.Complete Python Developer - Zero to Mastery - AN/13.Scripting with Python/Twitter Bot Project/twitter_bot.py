import tweepy
import configparser
import time

#load config from properties file
config = configparser.RawConfigParser()
config.read('twitter.properties')
consumer_key = config.get('AppSetting','consumer.API.key')
consumer_secret = config.get('AppSetting','consumer.API.secret.key')
access_token = config.get('AppSetting','access.token')
access_token_secret = config.get('AppSetting','access.token.secrect')

#tweepy configuration
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#home page tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#user profile
user = api.me()

#follow back the follower
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    follower.follow()

#like my own tweet
numberOfTweets = 2
search = 'java'
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        print(tweet)
        tweet.favorite()
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break