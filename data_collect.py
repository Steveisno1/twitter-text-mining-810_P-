import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

consumer_key = "Rjv6bl6fhdo8sxZ5ws9KlSWRl"
consumer_secret = "n9X6PjvrG8xzFNxuddLI8GcL5oVlRIY0r18T4mqrj4poaMwJWX"
access_token = "3400972894-6JhhZNMebKdKzXpeh8iT1DGSnzdFVvPrSnthI0x"
access_secret = "Pvs7u7AFMO5nxoOR6KJRHh3GZ1SirKCTwtIl7ACUm1jz6"

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    
    def on_error(self, status):
        print status


if __name__ == '__main__':
    
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['spurs', 'thunder'])