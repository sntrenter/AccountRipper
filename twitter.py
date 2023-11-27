import tweepy
from twitterkeys import APIKEY, APIKEYSECRET, ACCESSTOKEN, ACCESSTOKENSECRET, BEARERTOKEN
consumer_key = APIKEY
consumer_secret = APIKEYSECRET
access_token = ACCESSTOKEN
access_token_secret = ACCESSTOKENSECRET
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# If the authentication was successful, this should print the
# screen name / username of the account
print(api.verify_credentials().screen_name)


bearer_token = BEARERTOKEN

client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("Tweepy")
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)

