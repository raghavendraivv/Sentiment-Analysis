import twitter

consumer_key = "0PUaJu0HnaUopQj9cAk8qO86V"
consumer_secret = "RtBy0xyTJTaGm4Ck7JRDnhja2GBDyr8q5PSdrWiIpaBxMCUHID"
access_key = "1341421482-QlzsdzLRE2ijEGajPjE48SAIbmya5NRobW4cSQn"
access_secret = "sqOFIG9J6lTrTy5Q763uXpNP25GvkFQj2BWSvuNYPjSyN"

auth = twitter.oauth.OAuth(access_key,access_secret,consumer_key,consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

trend = twitter_api.trends.place(_id=23424848)

for i in trend[0]['trends']:
    r = i['name'],'   ', i['tweet_volume']
    print(r)
