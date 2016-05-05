import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_path='Your file path'

tweets_data=[]
tweets_file=open(tweets_path,"r")

for line in tweets_file:
    try:
        #line = tweets_file.readline()
        tweet = json.loads(line)
        for thing in tweet:
            if 'text' in thing:
                tweets_data.append(tweet)
        #print(json.dumps(tweet, indent=4))
    except:
        continue
print('the number of tweets we got:')
print (len(tweets_data))
print('\n')

#for thing in tweets_data:
#    if 'text' not in thing:
#        tweets_data.remove(thing)
#print(len(tweets_data))


'''
tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'],tweets_data) #except: continue
''''''
tweets['lang'] = map(lambda tweet: tweet['lang'],tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None,tweets_data)

tweets_by_lang = tweets['lang'].value_counts()

#plot the top 5 languages
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
plt.show()
'''
#print(tweets['text'])
thunder = []
spurs = []
#tweets = pd.DataFrame()
#for tweet in tweets_data:
#    if tweet['text'] in tweet:
#        tweets['text'] = map(lambda tweet: tweet['text'],tweets_data)
if(map(lambda tweet: tweet['text'],tweets_data)):
    for item in map(lambda tweet: tweet['text'],tweets_data):
        item = item.lower()
    #print(item)
        if 'thunder' in item:
            thunder.append(item)
        if 'spur' in item:
            spurs.append(item)

'''print('\n')
for item in thunder:
    print(item)
print(len(thunder))
print('\n')

for item in spurs:
    print(item)
print(len(spurs))
print('\n')
'''

from nltk.tokenize import TweetTokenizer

#tweet_w=spurs[0]
#print(spurs[0])
s_tknzrs = TweetTokenizer()
s_terms=[]
for line in spurs:
    for word in s_tknzrs.tokenize(line):
        s_terms.append(word)
#print(tknzrs.tokenize(spurs[0]))

#terms.append('he')
#terms.append('to')

from nltk.corpus import stopwords
import string
#import nltk

#nltk.download("stopwords")
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'spurs', 'thunder', 'vs', 'game', 'soccer', 'tottenham']

s_nostop=[]
for term in s_terms:
    if term not in stop:
        s_nostop.append(term)

s_hashtag = []
for term in s_terms:
    if term not in stop:
        if '#' in term:
            s_hashtag.append(term)

s_terms_only = []
for term in s_terms:
    if term not in stop:
        if ('#' not in term) and ('@' not in term):
            s_terms_only.append(term)

from collections import Counter
s_count_nostop = Counter()
s_count_nostop.update(s_nostop)

s_count_hashtag = Counter()
s_count_hashtag.update(s_hashtag)

s_count_onlyterm = Counter()
s_count_onlyterm.update(s_terms_only)
'''
#for term in terms:
#    freqs=[(term, terms.count(term))]
#    occur.append(freqs)
'''
#print(s_terms)
print('number of terms with spurs:')
print(len(s_terms))
print('\n')
print('top 20 common terms including stop word with spurs')
print(s_count_nostop.most_common(20))
#print(s_nostop)

print('\n')
print('top 15 common hashtag with spurs')
print(s_count_hashtag.most_common(15))
#print(s_hashtag)

print('\n')
print('top 20 common terms within spurs')
print(s_count_onlyterm.most_common(20))
#print(s_terms_only)


t_tknzrs = TweetTokenizer()
t_terms=[]
for line in thunder:
    for word in t_tknzrs.tokenize(line):
        t_terms.append(word)
#print(tknzrs.tokenize(spurs[0]))

#terms.append('he')
#terms.append('to')

#from nltk.corpus import stopwords
#import string
#import nltk

#nltk.download("stopwords")
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'spurs', 'thunder', 'vs', 'game', 'soccer',
                                                   'tottenham', 'okc', '...', 'points', 'pts']

t_nostop=[]
for term in t_terms:
    if term not in stop:
        t_nostop.append(term)

t_hashtag = []
for term in t_terms:
    if term not in stop:
        if '#' in term:
            t_hashtag.append(term)

t_terms_only = []
for term in t_terms:
    if term not in stop:
        if ('#' not in term) and ('@' not in term):
            t_terms_only.append(term)



t_count_nostop = Counter()
t_count_nostop.update(t_nostop)

t_count_hashtag = Counter()
t_count_hashtag.update(t_hashtag)

t_count_onlyterm = Counter()
t_count_onlyterm.update(t_terms_only)
'''
#for term in terms:
#    freqs=[(term, terms.count(term))]
#    occur.append(freqs)
'''
#print(t_terms)
print('\n')
print('number of terms with thunder:')
print(len(t_terms))
print('\n')
print('top 20 common terms including stop word with thunder:')
print(t_count_nostop.most_common(20))
#print(t_nostop)

print('\n')
print('top 15 hashtags with thunder:')
print(t_count_hashtag.most_common(15))
#print(t_hashtag)

print('\n')
print('top 20 terms with thunder:')
print(t_count_onlyterm.most_common(20))
#print(t_terms_only)



