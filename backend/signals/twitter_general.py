# twitter sentiment analysis
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re 
import pandas as pd

analyzer = SentimentIntensityAnalyzer()

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


# Clean a function to clean tweets 
def cleanTweets(tweet, ticker):
  # Removes hashtags
  hashtag = f"#{ticker}"
  tweet = re.sub(hashtag , ticker, tweet)
  tweet = re.sub(hashtag, ticker.capitalize(), tweet)
  tweet = re.sub('#[A-Za-z0-9]+', '', tweet)
  # Removes \n and hyperlinks
  tweet = re.sub('\\n', '', tweet)
  tweet = re.sub('https?:\/\/S+', '', tweet)
  return tweet

# Create a function to get the polarity
def getPolarity(tweet):
  sentiment = analyzer.polarity_scores(tweet)
  return sentiment["compound"]

def get_score(ticker):
  search_term = f"#{ticker} -filter:retweets"
  tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang="en", since="2018-11-01", tweet_mode="extended").items(20)
  all_tweets = [tweet.full_text for tweet in tweets]

  cleaned_tweets = []
  for tweet in all_tweets:
    cleaned_tweets.append(cleanTweets(tweet, ticker))

  scores = []
  for tweet in cleaned_tweets:
    scores.append(getPolarity(tweet))

  if len(scores) == 0:
    return None
  else:
    avg = sum(scores)/len(scores)
    return avg