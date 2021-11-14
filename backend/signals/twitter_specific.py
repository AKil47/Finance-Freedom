# Twitter sentiment analysis
import tweepy
from textblob import TextBlob
import re 
import pandas as pd

# Twitter API Credentials
consumerKey = "qT6FW61JDZTFlBetQE4ClswMr"
consumerSecret = "xaK5NgoplobsYGexyVqkXFbGHj7Zwb87BN92zLMlvmvMNrqD4K"
accessToken = "1212555051933155328-5leWwyt1pOradkBFKjy189c7URubEM"
accessTokenSecret = "cgyFGIjGNeghqx5k8kLX5hfiJAHKessZugl3gacFZR3Jj"

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
# Set the access token and access token secrete
authenticate.set_access_token(accessToken, accessTokenSecret)
# Create the API object while passing in the auth info
api = tweepy.API(authenticate, wait_on_rate_limit = True)

def getPolarity(tweet):
  return TextBlob(tweet).sentiment.polarity

def get_score(user_name, ticker):
  posts = api.user_timeline(screen_name = user_name, count=30, lang='en', tweet_mode='extended')
  user_tweets = []
  for tweet in posts[0:30]:
    user_tweets.append(tweet.full_text)
  user_tweets = filter(lambda tweet: ticker in tweet, user_tweets)
  scores = []
  for tweet in user_tweets:
    scores.append(getPolarity(tweet))
  if len(scores) == 0:
    return None
  else:
    avg = sum(scores)/len(scores)
    return avg