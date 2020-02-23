import json
import tweepy
from TwitterAPI import config
def get_tweets(book,author):
    print(author)
    tweet_urls = []
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    for tweet in tweepy.Cursor(api.search,q='#'+book+' AND #book',lang="en").items(100):
      for url in tweet.entities['urls']:
         if "twitter" in url['expanded_url']:
            tweet_urls.append(str(tweet.id))
    if len(tweet_urls)==0:
        for tweet in tweepy.Cursor(api.search, q=author, lang="en").items(100):
            for url in tweet.entities['urls']:
                if "twitter" in url['expanded_url']:
                    tweet_urls.append(str(tweet.id))
    return json.dumps(tweet_urls)