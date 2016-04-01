import json, tweepy, os, sys, getopt, codecs
import config
from azure.servicebus import ServiceBusService
from tweepy import OAuthHandler
from time import sleep

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_secret

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):

        # Twitter returns data in JSON format - we need to decode it first
		decoded = json.loads(data)

        # # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        # print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        # print ''
        # return True

		sbs = ServiceBusService(service_namespace=config.servns, shared_access_key_name=config.key_name, shared_access_key_value=config.key_value)
		searched_tweets = "{ 'source': '" + unicode(decoded['user']['screen_name']) + "' , 'text': '" + unicode(decoded['text'].encode('ascii', 'ignore')) + "' }"
		print(unicode(searched_tweets))
		sbs.send_event('iot', unicode(searched_tweets))

		return True

    def on_error(self, status):
		print status
		return False

def main(args):
	query = ""

	opts, args = getopt.getopt(args,'q:')
	for opt, arg in opts:
		if opt == '-q':
   			query = arg

	l = StdOutListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	# print "Showing all new tweets for #" + query

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis

    
	stream = tweepy.Stream(auth, l)
	# stream.userstream
	stream.filter(track=[query], async=True)

	return 0

if __name__ == '__main__':

	sys.exit(main(sys.argv[1:]))



