#!/bin/python

import urllib.request
import json
import sys
import time
from functools import reduce

if len(sys.argv) != 1:
	config = json.load(open(sys.argv[1]))
	with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=0") as f:
		res = f.read()
		json_res = json.loads(res.decode())
	currencies = filter(lambda x: x['symbol'] in config.keys(), json_res)
	sum = 0
	timestamp = time.time()
	output = {'time': timestamp}
	output['balances'] = dict()
	output['rates'] = dict()
	for curr in currencies:
		value = float(curr['price_usd']) * float(config[curr['symbol']])
		#print("{0} {1}: {2:.2f} USD".format(config[curr['symbol']],curr['symbol'],value))
		#sum+=value
		output['balances'][curr['symbol']]= value
		output['rates'][curr['symbol']] = float(curr['price_usd'])
	#print("total balance = {0:.2f} USD".format(sum))
	json_string = json.dumps(output,indent=4)
	print(json_string)
	json_out = json.loads(json_string)
	#print( json_out['balances'].values())
	sum = reduce(lambda x,y: x+y, json_out['balances'].values())
	print(sum)
else:
	print("usage: python " + sys.argv[0] + " config.json")
	
