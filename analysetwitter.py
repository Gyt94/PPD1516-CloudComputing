import tweepy
import json
import os, sys
from azure.servicebus import ServiceBusService
from tweepy import OAuthHandler
from time import sleep

#Variables de configuration

servns = 'Miage2016' # service_bus _namespace
key_name = 'manage'
key_value = 'KEOU/Qun1wrPFO8eLXM4HCEa59WDP2qLcuuhNapYEjQ='  # SharedAccessKey from Azure portal
sbs = ServiceBusService(service_namespace=servns,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value) # Create a ServiceBus Service Object

access_token = '4832196184-FY45HwZRH3d9fNFAcc8tbdwBonqAoPNtCmaQX3C'
access_secret = '3i271smaOXbpDJ33mSzql90uHQXXe3POnPIWxkq3zirML'
consumer_key = 'njSeydg32gT3ezDvCNrn584CB'
consumer_secret = 'S2uj20xoQXW3Ae35MGRMgPmuv2KgNwlFjrhXLgpHIKKUthrclM'

query = ''
max_tweets = 40

#Fin Variables de configuration

#Code 

query = sys.argv[1]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

searched_tweets = [status._json for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
searched_tweets = json.dumps(searched_tweets)
sbs.send_event('iot', searched_tweets)

# for result in tweepy.Cursor(api.search, q=query).items():
#     sbs.send_event('iot', result)
#     sleep(1)

print("Finished")