
from azure.servicebus import ServiceBusService
import json,codecs
import feedparser
import time
import config


cpt = 0
sbs = ServiceBusService(service_namespace=config.servns,
                        shared_access_key_name=config.key_name,
                        shared_access_key_value=config.key_value) # Create a ServiceBus Service Object
temps=time.time()
chars_to_remove = ['\'']
europe = feedparser.parse('http://www.europe1.fr/var/export/rss/europe1/actus.xml')
dernE = europe.entries[0]
jason = "{'source':'europe1',\'title\':\'"+unicode(dernE.title)+"\','text':'"+unicode(dernE.description)+"'}"
#print(unicode(jason))
sbs.send_event('iot', unicode(jason))
france24 = feedparser.parse('http://www.france24.com/fr/france/rss')
dernLM= france24.entries[0]
jasonLM = "{'source':'france24',\'title\':\'"+unicode(dernLM.title)+"\','text':'"+unicode(dernLM.description)+"'}"
#print(unicode(jasonLM))
sbs.send_event('iot', unicode(jasonLM))
while True:
    europe = feedparser.parse('http://www.europe1.fr/var/export/rss/europe1/actus.xml')
    france24 = feedparser.parse('http://www.france24.com/fr/france/rss')
    if dernE != europe.entries[0]:
        dernE = europe.entries[0]
        jason = "{'source':'europe1',\'title\':\'"+unicode(dernE.title)+"\','text':'"+unicode(dernE.description)+"'}"
        #print(unicode(jason))
        sbs.send_event('iot', unicode(jason))
    if dernLM != france24.entries[0]:
        dernLM = france24.entries[0]
        #jasonLM = "{'source':'france24',\'title\':\'"+dernLM.title.replace('\'','')+"\','text':'"+dernLM.description.replace('\'','')+"'}"
        jasonLM = "{'source':'france24',\'title\':\'"+unicode(dernLM.title)+"\','text':'"+unicode(dernLM.description)+"'}"
        #print(unicode(jasonLM))
        sbs.send_event('iot', unicode(jasonLM))
    cpt=cpt+1
    print("boucle")
    time.sleep(30)

#from time import sleep
#for e in o :
#    print(json.dumps(e))
#    cpt = cpt + 1
#    sbs.send_event('iot', json.dumps(e))
#    sleep(1)
#print(cpt)
#print("Finished")
#