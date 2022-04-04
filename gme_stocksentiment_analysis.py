from logging import PlaceHolder
from numpy import negative
from textblob import TextBlob
import tweepy
import sys

#replace keys with actual values when using
api_key = PlaceHolder
api_key_secret = PlaceHolder
bearer_token = PlaceHolder
access_token = PlaceHolder
access_token_secret = PlaceHolder

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

#searching twitter for tweets about gamestop to gauge sentiment around recent stock surge
search_term = 'gamestop'
tweet_amount = 10

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)

polarity = 0

positive = 0
neutral = 0
negative = 0

#removing unneccessary information to try to get more accurate sentiment readings such as user handles
for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index('')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0:
        positive +=1
    elif tweet_polarity < 0:
        negative += 1
    else:
        neutral += 1
    polarity += analysis.polarity

#polarity rating and total number of tweets classified under certain polarities 
print(polarity)
print(f'amount of positive tweets: {positive}')
print(f'amount of negative tweets: {negative}')
print(f'amount of neutral tweets: {neutral}')