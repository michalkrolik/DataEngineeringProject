from forex_python.converter import CurrencyRates
import pandas_datareader as web
import datetime
import pymongo
import json

CONFIG_LOCATION='./'
CONFIG = json.loads(open(str(CONFIG_LOCATION+'config.json')).read())

mongo_username    = CONFIG['secrets']['mongo_username']
mongo_password    = CONFIG['secrets']['mongo_password']
mongo_database    = CONFIG['secrets']['mongo_database']
mongo_collection    = CONFIG['secrets']['mongo_collection']

c = CurrencyRates()

ts = datetime.datetime.now().timestamp()
today = datetime.datetime.now() - datetime.timedelta(hours=1, minutes=0)
today_formatted = today.strftime('%Y%m%d')

usd_price = c.get_rates('USD')['PLN']
eur_price = c.get_rates('EUR')['PLN']
gbp_price = c.get_rates('GBP')['PLN']
chf_price = c.get_rates('CHF')['PLN']
my_usd = c.convert('USD', 'PLN', 800)

btc = web.DataReader('BTC-USD', 'yahoo', today_formatted)
eth = web.DataReader('ETH-USD', 'yahoo', today_formatted)
xrp = web.DataReader('XRP-USD', 'yahoo', today_formatted)
btc_price_pln = btc.Close[0]*usd_price
eth_price_pln = eth.Close[0]*usd_price
xrp_price_pln = xrp.Close[0]*usd_price

myclient = pymongo.MongoClient("mongodb://mongodb:27017/", username=mongo_username, password=mongo_password)
mydb = myclient[mongo_database]
mycol = mydb[mongo_collection]

mydict = { "timestamp": str(ts), "usd_price": str(usd_price), "my_usd": str(my_usd), "btc_price_pln": str(btc_price_pln), "eth_price_pln": str(eth_price_pln), "xrp_price_pln": str(xrp_price_pln) }

print(mydict)
x = mycol.insert_one(mydict)
