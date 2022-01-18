# Twitter sentiment analysis
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import os

load_dotenv()

analyzer = SentimentIntensityAnalyzer()

# Twitter API Credentials
consumerKey = os.getenv("CONSUMER_KEY")
consumerSecret = os.getenv("CONSUMER_SECRET")
accessToken = os.getenv("ACCESS_TOKEN")
accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
# Set the access token and access token secrete
authenticate.set_access_token(accessToken, accessTokenSecret)
# Create the API object while passing in the auth info
api = tweepy.API(authenticate, wait_on_rate_limit = True)

def getPolarity(tweet):
  sentiment = analyzer.polarity_scores(tweet)
  return sentiment["compound"]

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

get_score("elonmusk", "Tesla")