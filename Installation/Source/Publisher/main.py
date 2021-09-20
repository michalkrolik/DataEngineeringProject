import pymongo
import json
from bson.json_util import dumps

CONFIG_LOCATION='./'
CONFIG = json.loads(open(str(CONFIG_LOCATION+'config.json')).read())
mongo_username    = CONFIG['secrets']['mongo_username']
mongo_password    = CONFIG['secrets']['mongo_password']

client = pymongo.MongoClient("mongodb://mongodb:27017/", username='ingestor', password='ingestor')

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

for players in ["Lewandowski","Mbappé","Messi","Ronaldo","Haaland"]:

        db = client[players]
        col = db[players]

        x = col.find({},{'_id': 0, 'timestamp': 1, 'Photo': 1, 'Age': 1, 'Country': 1, 'Team': 1, 'Goals': 1, 'Assists': 1, 'Appearences': 1, 'Minutes_played': 1, 'Yellow_cards': 1, 'Red_cards': 1, 'Penalty_missed': 1, 'Penalty_scored': 1})

        file_name = players
        if players == "Mbappé":
            file_name = "Mbappe"

        Path("/app/football").mkdir(parents=True, exist_ok=True)
        file_path='/app/football/'+file_name+'.json'

        with open(file_path, 'w') as file:
            file.write('[')
            for document in x:
                file.write(dumps(document))
                file.write(',')
            file.seek(0,2)
            file.seek(file.tell() - 2, 0)
            file.truncate()
            file.write('}]')
