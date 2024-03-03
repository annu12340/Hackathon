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


