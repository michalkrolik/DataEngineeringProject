from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import datetime
import pymongo

c = CurrencyRates()
b = BtcConverter()

ts = datetime.datetime.now().timestamp()
usd_price = c.get_rates('USD')['PLN']
my_usd = c.convert('USD', 'PLN', 800)
btc_price_pln = b.get_latest_price('PLN')
#print(str(ts)+","+str(usd_price)+","+str(my_usd)+","+str(btc_price_pln))

myclient = pymongo.MongoClient("mongodb://mongodb:27017/", username='user', password='password')
mydb = myclient["forex"]
mycol = mydb["forex"]

mydict = { "timestamp": str(ts), "usd_price": str(usd_price), "my_usd": str(my_usd), "btc_price_pln": str(btc_price_pln) }

#print(mydict)
x = mycol.insert_one(mydict)