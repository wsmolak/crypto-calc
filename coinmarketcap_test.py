import urllib.request
import json
import sys


if len(sys.argv) != 1:
	config = json.load(open(sys.argv[1]))
	with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/") as f:
		json = json.loads(f.read())
		currencies = filter(lambda x: x['symbol'] in config.keys(), json)
		sum = 0
		for curr in currencies:
			print(config[curr['symbol']]+" "+curr['symbol']+": "+ str( float(curr['price_usd']) * float(config[curr['symbol']]) ) + " USD")
			sum+=float(curr['price_usd']) * float(config[curr['symbol']])
		print("total balance = "+ str(sum) + " USD")
else:
	print("usage: python " + sys.argv[0] + " config.json")