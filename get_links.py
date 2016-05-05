import json
import pandas as pd
import matplotlib.pyplot as plt
import re

tweets_data_path = '/Users/Jhzhou/Desktop/easy/twitter_data.txt'


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


tweets_data = []
tweets_spurs = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

tweets['#spurs'] = tweets['text'].apply(lambda tweet: word_in_text('#spurs', tweet))
tweets['#thunder'] = tweets['text'].apply(lambda tweet: word_in_text('#thunder', tweet))
print tweets['#spurs'].value_counts()[True]
print tweets['#thunder'].value_counts()[True]

tweets['video'] = tweets['text'].apply(lambda tweet: word_in_text('video', tweet))
print tweets['video'].value_counts()[True]

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
tweets_relevant = tweets[tweets['video'] == True]

print tweets_relevant['link']

