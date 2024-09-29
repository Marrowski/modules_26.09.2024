import task1 as load
import json


with open('services.json', 'w') as new_f:
    new_f.write(json.dumps(load.dictionary_services))