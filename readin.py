import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token="3593527217-25yitR0zDZYuzXCqBI8PsCyDiktZdLf5tCqZwKp"
access_token_secret="iR15KFLGuGufU7zppeS4m3nIgadbblKtPMaNWFhszCouE"
consumer_key="7VCqUQnAvWZHGpzzZHsXhCe78"
consumer_secret="1yfKvbz2LA1f74bbqhBDL8N5oTDhAjTHyK3nudkZsn3QwgiqZd"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'thunder', 'spurs'.
    stream.filter(track=['thunder', 'spurs'])
    #8:00 PM to 11:15 pm, half hour before the match and 30 minutes after the match


