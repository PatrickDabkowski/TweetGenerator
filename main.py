import twitter
import json
# Creating API connection
ck = input('Put your CONSUMER_KEY:')
csk = input('CONSUMER_SECRET_KEY:')
ot = input('Put your OAUTH_TOKEN:')
ots = input('Put your OAUTH_TOKEN_SECRET:')
CONSUMER_KEY = ck
CONSUMER_SECRET_KEY = csk
OAUTH_TOKEN = ot
OAUTH_TOKEN_SECRET = ots
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY)
twitter_api = twitter.Twitter(auth=auth)
print(twitter_api)
# Getting Data
q = input("\nGet #:\n")
count = 100
from urllib.parse import unquote
search_reults = twitter_api.search.tweets(q=q, count = count)
statuse = search_reults['statuses']
for _ in range(5):
    print(end=" ")
    try:
        next_results = search_reults['search_metadata']['next_results']
    except KeyError as e: break
kwargs = dict([kv.split('=') for kv in unquote(next_results[1:]).split("&")])
search_results = twitter_api.search.tweets(**kwargs)
statuse += search_reults['statuses']

status_text = [status['text']
               for status in statuse]
words = [w
         for t in status_text
         for w in t.split()]
hashtags = [hashtags['text']
            for status in statuse
            for hashtags in status['entities']['hashtags']]
screen_name = [user_mentions['screen_name']
               for status in statuse
               for user_mentions in status['entities']['user_mentions']]

import random
# Creating Generated Tweet
def generate_tweet(user, hashtags, words):
    generatetweet = open('generatetweet.txt', 'w')
    user_t = random.choice(user)
    hashtags_t1 = hashtags[0]
    hashtags_t2 = random.choice(hashtags)
    hashtags_t3 = random.choice(hashtags)
    hashtags_t4 = hashtags[-1]
    print("\n@",user_t,"\n#", hashtags_t1, "\t#", hashtags_t2, "\t#", hashtags_t3, "\t#", hashtags_t4)
    generatetweet.write("@"+str(user_t)+"\n#"+hashtags_t1+"\n#"+hashtags_t2+"\n#"+hashtags_t3+"\n#"+hashtags_t4+"\n")
    for _ in range(40):
        text = random.choice(words)
        print(text, end=" ")
        generatetweet.write(str(text)+" ")
    generatetweet.close()
generate_tweet(screen_name, hashtags, words)
