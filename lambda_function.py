import tweepy
import dotenv
import os
from dotenv import load_dotenv
load_dotenv()

######################################################################
## Environment variables

bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

######################################################################
### Main function

def lambda_handler(event, context): 

    # Authenticate to Twitter
    client = tweepy.Client(bearer_token=bearer_token,
                        consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token=access_token,
                        access_token_secret=access_token_secret) 

    # Create first tweet
    first_tweet = 'Hello World!'
    client.create_tweet(text=first_tweet)
    print("tweet published!")