# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import requests
import requests_oauthlib
from textblob import TextBlob
import tweepy
import nltk

access_token = "2721234898-yZ2dGB6nPo21ia09dUEtjblp7Q53Fh3usIimTto"
access_token_secret = "F8wmByokRFtHqCRECeD6MCELfMSGQIL0pASsjq5Reygmo"
consumer_key = "juxL77LAY5gXuuel5bayXM0v1"
consumer_secret = "ehsLrBNgQsjB4ySzSiuJ1bvaitS5om96WQDo8VBmJivuQHLBnD"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
public_tweets = api.search('Basketball')

avgsubjectivity = 0
avgpolarity = 0
count = 0 

for tweets in public_tweets:
	print(tweets.text)
	analysis = TextBlob(tweets.text)
	tweetsubjectivity = analysis.subjectivity
	tweetpolarity = analysis.polarity
	count += 1
	avgsubjectivity += tweetsubjectivity
	avgpolarity += tweetpolarity
	print("Tweet Subjectivity: ", tweetsubjectivity)
	print("Tweet Polarity: ", tweetpolarity)


print("Average Subjectivity: ", (avgsubjectivity / count))
print("Average Polarity: ", (avgpolarity / count))