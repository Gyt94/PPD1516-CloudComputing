from azure.servicebus import ServiceBusService
import json,codecs
import feedparser
import time
import config

while True:
    france24 = feedparser.parse('http://www.lemonde.fr/rss/une.xml')
    dernLM= france24.entries[0]
    jasonLM = "{'source':'france24',\'title\':\'"+unicode(dernLM.title)+"\','text':'"+unicode(dernLM.description)+"'}"
    print( jasonLM.encode('cp850', errors='replace'))
    time.sleep(30)