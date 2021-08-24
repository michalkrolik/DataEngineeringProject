import pymongo
import json
from bson.json_util import dumps

CONFIG_LOCATION='./'
CONFIG = json.loads(open(str(CONFIG_LOCATION+'config.json')).read())
mongo_username    = CONFIG['secrets']['mongo_username']
mongo_password    = CONFIG['secrets']['mongo_password']

client = pymongo.MongoClient("mongodb://mongodb:27017/", username=mongo_username, password=mongo_password)

db = client["forex"]
col = db["forex"]

#x = col.find()
x = col.find({},{'_id': 0, 'timestamp': 1, 'usd_price': 1, 'my_usd': 1, 'btc_price': 1, 'btc_price_pln': 1, 'eth_price': 1, 'eth_price_pln': 1, 'xrp_price': 1, 'xrp_price_pln': 1, 'hbar_price': 1, 'hbar_price_pln': 1})

#for row in x:
#    print(row)

with open('/app/forex.json', 'w') as file:
    file.write('[')
    for document in x:
        file.write(dumps(document))
        file.write(',')
    file.seek(0, 2)
    file.seek(file.tell() - 2, 0)
    file.truncate()
    file.write('}]')


