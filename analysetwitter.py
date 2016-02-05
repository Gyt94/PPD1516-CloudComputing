import json, tweepy, os, sys, getopt, codecs
import config
from azure.servicebus import ServiceBusService
from tweepy import OAuthHandler
from time import sleep

#Variables de configuration

sbs = ServiceBusService(service_namespace=config.servns,
                        shared_access_key_name=config.key_name,
                        shared_access_key_value=config.key_value) # Create a ServiceBus Service Object

max_tweets = 20

arg_query = ''
arg_tweet_id = 10000
arg_time = 60

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
 
api = tweepy.API(auth)

opts, args = getopt.getopt(sys.argv[1:],'q:t:')
for opt, arg in opts:
	# en travaux : changer entre mode requete et timeline
   if opt == '-q':
      arg_query = arg
   elif opt == '-t':
      arg_time = float(arg)

# if arg_query == '':
tweet_id = arg_tweet_id
while True:
	i = 0
	for status in tweepy.Cursor(api.home_timeline, since_id = tweet_id).items(max_tweets):
		if i == 0:
			last_tweet_id = status.id
		# print(unicode(status.text))
		print("tweet : " + str(status.id))
		searched_tweets = "{ 'source': '" + unicode(status.user.name) + "' , 'text': '" + unicode(status.text) + "' }"
		print(unicode(searched_tweets))
		sbs.send_event('iot', unicode(searched_tweets))
		i = i + 1

	tweet_id = last_tweet_id
	print('dodo' + ' id : ' + str(last_tweet_id))
	sleep(arg_time)

# else:
# searched_tweets = [status._json for status in tweepy.Cursor(api.home_timeline).items(max_tweets)]
# searched_tweets = json.dumps(searched_tweets)
# sbs.send_event('iot', searched_tweets)

# for result in tweepy.Cursor(api.search, q=query).items():
#     sbs.send_event('iot', result)
#     sleep(1)
