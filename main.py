import tweepy
import json
import pandas as pd

CONSUMER_KEY = 'tdfdfgdgsc'
CONSUMER_SECRET = 'dsfsfddsf'
ACCESS_TOKEN = 'sfcxvxcfv'
ACCESS_TOKEN_SECRET = 'cvbsdfsdf'

def accept_tweet(tweet):
    THRESHOLD = 3
    interactions = tweet['retweet_count'] + tweet['favorite_count']
    if interactions >= THRESHOLD and 'RT ' not in tweet['full_text']:
        return True
    return False

def calculate_popularity(tweet):
    pond_public_list = 7
    pond_tweet_interaction = 5
    pond_follower_number = 1
    user = tweet['user']
    tweet_interactions = tweet['retweet_count'] + tweet['favorite_count']
    return (pond_public_list * user['listed_count']) + (pond_tweet_interaction * tweet_interactions) + (pond_follower_number * user['followers_count']) + 1

def normalize_popularity(popularity, min_popularity, max_popularity):
    return 100 * (popularity - min_popularity) / (max_popularity - min_popularity)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
min_popularity = 0
max_popularity = 0
tweets = []
for tweet_parsed in tweepy.Cursor(api.search, q="#ParoDeTransportistas",tweet_mode="extended").items(7000):
    tweet_str= json.dumps(tweet_parsed._json,indent=2)
    tweet = tweet_parsed._json
    if accept_tweet(tweet):
        tweet_data = {
            'user_id': tweet['user']['id_str'],
            'user_name': tweet['user']['name'],
            'popularity': calculate_popularity(tweet),
            'user_location': tweet['user']['location'],
            'tweet_msg': tweet['full_text']
        }
        tweets.append(tweet_data)
        if max_popularity == 0:
            min_popularity = tweet_data['popularity']
            max_popularity = tweet_data['popularity']
            continue
        if tweet_data['popularity'] < min_popularity:
            min_popularity = tweet_data['popularity']
        elif tweet_data['popularity'] > max_popularity:
            max_popularity = tweet_data['popularity']

tweets_analyzed = []
for tweet in tweets:
    tweet['popularity'] = normalize_popularity(tweet['popularity'], min_popularity, max_popularity)
    tweets_analyzed.append(tweet)

tweet_str = json.dumps(tweets_analyzed, indent=2)

print(tweet_str)

# archivo="datos_twiter.csv"
# csv=open(archivo,"w")
# titles="user_id,user_name,popularity,user_location,tweet_msg"






# Algunos strings estan codificados, nose en que, y algunos caracteres salen como estos "#PER\u00da / EUROPA / #ASIA / LatAm", aqui \u00da seria igual a Ú,
# Antes de usuarlos seria decodificar esos strings a lo que pertenescan, derre es utf-8

# Normalice la popularidad para que vaya de 0 a 100 y sea mas facil de graficar
