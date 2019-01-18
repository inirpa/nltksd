from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
	
# from twitterapistuff import *

#consumer key, consumer secret, access token, access secret.
ckey="GPf9z41bb5f1cUGXZGJcTTvct"
csecret="BoILguGn8UcPWKnt5qR0aFsVa7Sg5M5F0ZWaKIndpwu3mfw2Ik"
atoken="725330079925043200-NzhEgRTjHX6A2FfLIsRtCXFe5kbqr5k"
asecret="jRvYVdVe0I7lpq40B0yAdcWwgwHtQyx5iKRY6fzPL6r1Q"

class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)

		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

    def on_error(self, status):
        print("error code" + status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["iphone"])