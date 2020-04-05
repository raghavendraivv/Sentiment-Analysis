import twitter

consumer_key = "-"
consumer_secret = "-"
access_key = "-"
access_secret = "-"

auth = twitter.oauth.OAuth(access_key,access_secret,consumer_key,consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

trend = twitter_api.trends.place(_id=23424848)

for i in trend[0]['trends']:
    r = i['name'],'   ', i['tweet_volume']
    print(r)
