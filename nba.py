###########################################################
import re

emoticons_str = r"""
    (?:
    [:=;] # Eyes
    [oO\-]? # Nose (optional)
    [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
             emoticons_str,
             r'<[^>]+>', # HTML tags
             r'(?:@[\w_]+)', # @-mentions
             r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
             r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
             
             r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
             r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
             r'(?:[\w_]+)', # other words
             r'(?:\S)' # anything else
             ]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

############################################################
from nltk.corpus import stopwords
from nltk import bigrams
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
############################################################

import operator
import json
from collections import Counter
import pandas as pd
import pandas
import matplotlib.pyplot as plt

tweets_data_path = '/Users/Jhzhou/Desktop/easy/match.json'
#
tweets_data = []
#retweets = []
#lang = []
tweets_file = open(tweets_data_path, "r")
#for line in tweets_file:
#    try:
#        tweet = json.loads(line)
#        if tweet.has_key('retweeted_status'):
#            retweets.append(tweet['retweeted_status']['text'])
#        lang.append(tweet['lang'])
#        if tweet['place'] != None:
#            country.append(tweet['place'])
#        tweets_data.append(tweet)
#    except:
#        continue
#
#print(len(tweets_data))

#tweets = pd.DataFrame()

#tweet['text'] = map(lambda tweet: tweet['text'], tweets_data)
#
#tweets['']

#tweets['retweet'] = retweets
#print tweets['retweet'].value_counts()[:20]

#tweets['lang'] = lang
#print tweets['lang'].value_countes()[:5]

################################################################
################################################################

count_all = Counter()
count_single = Counter()
count_hash = Counter()
count_only = Counter()
count_bigram = Counter()
count_stop_single = Counter()

for line in tweets_file:
    try:
        tweet = json.loads(line)
        terms_all = [term for term in preprocess(tweet['text'])]
        terms_single = set(terms_all)
        terms_stop = [term.lower() for term in preprocess(tweet['text']) if term not in stop]
        terms_hash = [term.lower() for term in preprocess(tweet['text'])
                      if term.startswith('#')]
        terms_only = [term.lower() for term in preprocess(tweet['text'])
                                    if term not in stop and
                                    not term.startswith(('#', '@'))]
        terms_stop_single = set(terms_stop)
        terms_bigram = bigrams(terms_stop)
        
        count_all.update(terms_all)
        count_single.update(terms_single)
        count_hash.update(terms_hash)
        count_only.update(terms_only)
        count_bigram.update(terms_bigram)
        count_stop_single.update(terms_stop_single)
    except:
        continue

print('count_all.most_common(20)')
print json.dumps(count_all.most_common(20))
print
print('count_single.most_common(20)')
print json.dumps(count_single.most_common(20))
print
print('count_hash.most_common(20)')
print json.dumps(count_hash.most_common(20))
print
print('count_only.most_common(20)')
print json.dumps(count_only.most_common(20))
print
print('count_bigram.most_common(20)')
print count_bigram.most_common(20)


################################################################


#print tweets_by_text[:10]

#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=15)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Languages', fontsize=15)
#ax.set_ylabel('Number of tweets' , fontsize=15)
#ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
#tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
#plt.show()

#tweets_by_country = tweets['country'].value_counts()
#
#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=15)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Countries', fontsize=15)
#ax.set_ylabel('Number of tweets' , fontsize=15)
#ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
#tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
#
#plt.show()

################################################################
################################################################

import re

#def word_in_text(word, text):
#    word = word.lower()
#    text = text.lower()
#    match = re.search(word, text)
#    if match:
#        return True
#    return False

#tweets['spurs'] = tweets['text'].apply(lambda tweet: word_in_text('spurs', tweet))
#tweets['thunder'] = tweets['text'].apply(lambda tweet: word_in_text('thunder', tweet))

#
#print tweets['spurs'].value_counts()[True]
#print tweets['thunder'].value_counts()[True]
#
#
#def extract_link(text):
#    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
#    match = re.search(regex, text)
#    if match:
#        return match.group()
#    return ''
#
#tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
#tweets['video'] = tweets['text'].apply(lambda tweet: word_in_text('video', tweet))
#
#tweets_video = tweets[tweets['video'] == True]
#tweets_video_with_link = tweets_video[tweets_video['link'] != '']
#
#print tweets_video_with_link[tweets_video_with_link['spurs'] == True]['link']



################################################################
################################################################
#import vincent
#
#word_freq = count_hash.most_common(20)
#labels, freq = zip(*word_freq)
#data = {'data': freq, 'x': labels}
#bar = vincent.Bar(data, iter_idx='x')
#bar.to_json('term_freq.json', html_out=True, html_path='chart.html')


################################################################
#fail
################################################################
#import pandas
#import json
#
#dates_ITAvWAL = []
## f is the file pointer to the JSON data set
#for line in tweets_file:
#    try:
#        tweet = json.loads(line)
#    # let's focus on hashtags only at the moment
#        terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
#    # track when the hashtag is mentioned
#        if '#NBAplayoffs' in terms_hash:
#            dates_ITAvWAL.append(tweet['created_at'])
#    except:
#        continue
#
## a list of "1" to count the hashtags
#ones = [1]*len(dates_ITAvWAL)
## the index of the series
#idx = pandas.DatetimeIndex(dates_ITAvWAL)
## the actual series (at series of 1s for the moment)
#ITAvWAL = pandas.Series(ones, index=idx)
#
## Resampling / bucketing
#per_minute = ITAvWAL.resample('1Min', how='sum').fillna(0)
#
#time_chart = vincent.Line(ITAvWAL)
#time_chart.axis_titles(x='Time', y='Freq')
#time_chart.to_json('time_chart.json', html_out=True, html_path='chart.html')

################################################################
#fail
################################################################

#geo_data = {
#    "type": "FeatureCollection",
#        "features": []
#}
#for line in tweets_file:
#    try:
#        tweet = json.loads(line)
#        if tweet['coordinates']:
#            geo_json_feature = {
#                "type": "Feature",
#                "geometry": tweet['coordinates'],
#                "properties": {
#                    "text": tweet['text'],
#                    "created_at": tweet['created_at']
#                }
#            }
#            geo_data['features'].append(geo_json_feature)
#    except:
#        continue
#
#with open('geo_data.json', 'w') as fout:
#    fout.write(json.dumps(geo_data, indent=4))

################################################################
#sentiment
################################################################
from collections import defaultdict

p_t = {}
p_t_com = defaultdict(lambda : defaultdict(int))

for term, n in count_stop_single.items():
    p_t[term] = n / n_docs
    for t2 in com[term]:
        p_t_com[term][t2] = com[term][t2] / n_docs

positive_vocab = [
                  'good', 'nice', 'great', 'awesome', 'outstanding',
                  'fantastic', 'terrific', ':)', ':-)', 'like', 'love',
                  # shall we also include game-specific terms?
                  # 'triumph', 'triumphal', 'triumphant', 'victory', etc.
                  ]
negative_vocab = [
                  'bad', 'terrible', 'crap', 'useless', 'hate', ':(', ':-(',
                  # 'defeat', etc.
                  ]

pmi = defaultdict(lambda : defaultdict(int))
for t1 in p_t:
    for t2 in com[t1]:
        denom = p_t[t1] * p_t[t2]
        pmi[t1][t2] = math.log2(p_t_com[t1][t2] / denom)

semantic_orientation = {}
for term, n in p_t.items():
    positive_assoc = sum(pmi[term][tx] for tx in positive_vocab)
    negative_assoc = sum(pmi[term][tx] for tx in negative_vocab)
    semantic_orientation[term] = positive_assoc - negative_assoc

semantic_sorted = sorted(semantic_orientation.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
top_pos = semantic_sorted[:10]
top_neg = semantic_sorted[-10:]
print(top_pos)
print(top_neg)
################################################################
