import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb://mongodb:27017/", username='ingestor', password='ingestor')

db = client["forex"]
col = db["forex"]

#x = col.find()
x = col.find({},{'_id': 0, 'timestamp': 1, 'usd_price': 1, 'my_usd': 1, 'btc_price_pln': 1, 'eth_price_pln': 1, 'xrp_price_pln': 1})

#for row in x:
#    print(row)

with open('./forex.json', 'w') as file:
    file.write('[')
    for document in x:
        file.write(dumps(document))
        file.write(',')
    file.write(']')
