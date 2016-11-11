# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")


import tweepy
import nltk
import requests
import requests_oauthlib

access_token = "2721234898-yZ2dGB6nPo21ia09dUEtjblp7Q53Fh3usIimTto"
access_token_secret = "F8wmByokRFtHqCRECeD6MCELfMSGQIL0pASsjq5Reygmo"
consumer_key = "juxL77LAY5gXuuel5bayXM0v1"
consumer_secret = "ehsLrBNgQsjB4ySzSiuJ1bvaitS5om96WQDo8VBmJivuQHLBnD"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
img = "/Users/robertbracci/desktop/project3/SI206/friends.jpg" 
api.update_with_media(img, status="#UMSI-206 #Proj3")
print("Posted")