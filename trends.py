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

tweets_data_path = '/Users/Jhzhou/Desktop/easy/match.json'

tweets_data = []

count_all = Counter()
count_stop = Counter()
count_single = Counter()
count_hash = Counter()
count_only = Counter()
count_bigram = Counter()

tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        
        terms_all = [term for term in preprocess(tweet['text'])]
        count_all.update(terms_all)
        
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop and term.startswith('#')]
        count_stop.update(terms_stop)
        
        # Count terms only once, equivalent to Document Frequency
        terms_single = set(terms_all)
        count_single.update(terms_single)
        # Count hashtags only
        terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
        count_hash.update(terms_hash)
        # Count terms only (no hashtags, no mentions)
        terms_only = [term for term in preprocess(tweet['text']) if term not in stop and
                      not term.startswith(('#', '@'))]
                      count_only.update(terms_only)
                      
                      terms_bigram = bigrams(terms_stop)
                      count_bigram.update(terms_bigram)
    except:
        continue

print('count_all.most_common(20)')
print count_all.most_common(20)
print
print('count_stop.most_common(20)')
print count_stop.most_common(20)
print
print('count_single.most_common(20)')
print count_single.most_common(20)
print
print('count_hash.most_common(20)')
print count_hash.most_common(20)
print
print('count_only.most_common(20)')
print count_only.most_common(20)
print
print('count_bigram.most_common(20)')
print count_bigram.most_common(20)
#################################################