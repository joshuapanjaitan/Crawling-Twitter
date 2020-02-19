import tweepy
import numpy as np
import csv

consumer_key = 'your cs key'
consumer_secret = 'your cs secret'

access_key = 'your access_key'
access_secret = 'your access_secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

username = '@jooshpn'
store = api.user_timeline(screen_name=username,
                          count=5, tweet_mode='extended')


def numOfFollowers(username):  # jumlah folower
    ress = api.get_user(username)
    return ress.followers_count


def numOfFollowing(username):  # jumlah orang yang di follow
    ress = api.get_user(username)
    return ress.friends_count


print(numOfFollowers(username))
for tweet in store:
    tweet = tweet.full_text
