import twitter
import csv
import tweepy
import pandas as pd

consumer_key = "-"
consumer_secret = "-"
access_key = "-"
access_secret = "-"

auth = twitter.oauth.OAuth(access_key,access_secret,consumer_key,consumer_secret)

twitter_api = twitter.Twitter(auth=auth)
api = tweepy.API(auth,wait_on_rate_limit=True)
trend = twitter_api.trends.place(_id=23424848)

for i in trend[0]['trends']:
    r = i['name'],'   ', i['tweet_volume']
    print(r)

x=input()
csvFile = open('ua.csv', 'a')
try:
    print("Correct")
    feteched = twitter_api.GetSearch(x, count = 100)
    print(feteched + x)
except:
    print("Wrong")
