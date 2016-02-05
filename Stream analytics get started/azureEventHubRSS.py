
from azure.servicebus import ServiceBusService
import json
import feedparser
import time

servns = 'Miage2016' # service_bus _namespace
key_name = 'manage'  # SharedAccessKeyName from Azure portal
key_value = 'KEOU/Qun1wrPFO8eLXM4HCEa59WDP2qLcuuhNapYEjQ='  # SharedAccessKey from Azure portal
cpt = 0
sbs = ServiceBusService(service_namespace=servns,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value) # Create a ServiceBus Service Object
temps=time.time()
chars_to_remove = ['\'']
europe = feedparser.parse('http://www.europe1.fr/var/export/rss/europe1/actus.xml')
dernE = europe.entries[0]
jason = "{'source':'europe1',\'title\':\'"+dernE.title.replace('\'','')+"\','text':'"+dernE.description.replace('\'','')+"'}"

france24 = feedparser.parse('http://www.france24.com/fr/france/rss')
dernLM= france24.entries[0]
jasonLM = "{'source':'france24',\'title\':\'"+dernLM.title.replace('\'','')+"\','text':'"+dernLM.description.replace('\'','')+"'}"
print jason
print jasonLM

while True:
    europe = feedparser.parse('http://www.europe1.fr/var/export/rss/europe1/actus.xml')
    france24 = feedparser.parse('http://www.france24.com/fr/france/rss')
    if dernE != europe.entries[0]:
        dernE = europe.entries[0]
        jason = "{'source':'europe1',\'title\':\'"+dernE.title.replace('\'','')+"\','text':'"+dernE.description.replace('\'','')+"'}"
        print jason
    if dernLM != france24.entries[0]:
	    dernLM = france24.entries[0]
	    jasonLM = "{'source':'france24',\'title\':\'"+dernLM.title.replace('\'','')+"\','text':'"+dernLM.description.replace('\'','')+"'}"
	    print jasonLM
    time.sleep(60)

#from time import sleep
#for e in o :
#    print(json.dumps(e))
#    cpt = cpt + 1
#    sbs.send_event('iot', json.dumps(e))
#    sleep(1)
#print(cpt)
#print("Finished")
#