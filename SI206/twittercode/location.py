import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Gilmore Girls" geocode:40.6781784,-73.94415789999999,10km')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
