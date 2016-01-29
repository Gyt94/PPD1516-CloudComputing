
from azure.servicebus import ServiceBusService
import json


servns = 'Miage2016' # service_bus _namespace
key_name = 'manage'  # SharedAccessKeyName from Azure portal
key_value = 'KEOU/Qun1wrPFO8eLXM4HCEa59WDP2qLcuuhNapYEjQ='  # SharedAccessKey from Azure portal
cpt = 0
sbs = ServiceBusService(service_namespace=servns,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value) # Create a ServiceBus Service Object

with open('telco.json') as f:
    o=json.load(f)

from time import sleep
for e in o :
    print(json.dumps(e))
    cpt = cpt + 1
    sbs.send_event('iot', json.dumps(e))
    sleep(1)
print(cpt)
print("Finished")
