import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

print(consumer_key, consumer_secret, access_token, access_token_secret)
if None in (consumer_key, consumer_secret, access_token, access_token_secret):
    raise ValueError("Please set all Twitter API credentials in environment variables")


# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Hashtag to search for
hashtag = '#woman'

# Number of tweets to retrieve
count = 10

# Retrieve tweets with the hashtag
tweets = api.search_tweets(q=hashtag, count=count)

# Print the tweets
for tweet in tweets:
    print(tweet.text)