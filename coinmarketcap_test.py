import urllib.request
import json
import sys

if len(sys.argv) != 1:
	config = json.load(open(sys.argv[1]))
	#print(config.keys())
	with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=0") as f:
		json = json.loads(f.read())
		currencies = filter(lambda x: x['symbol'] in config.keys(), json)
		sum = 0
		for curr in currencies:
			value = float(curr['price_usd']) * float(config[curr['symbol']])
			print("{0} {1}: {2:.2f} USD".format(config[curr['symbol']],curr['symbol'],value))
			sum+=value
		print("total balance = {0:.2f} USD".format(sum))
else:
	print("usage: python " + sys.argv[0] + " config.json")
