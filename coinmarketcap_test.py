import urllib.request
import json
import sys

if len(sys.argv) != 1:
    config = json.load(open(sys.argv[1]))
    proxies = config['proxy']
    if proxies != "None":
        opener = urllib.request.FancyURLopener(proxies)
    else:
        opener = urllib.request.FancyURLopener({})
    with opener.open("https://api.coinmarketcap.com/v1/ticker/?limit=0") as f:
        res = f.read()
        json = json.loads(res.decode())
        currencies = filter(lambda x: x['symbol'] in config.keys(), json)
        sum = 0
        for curr in currencies:
            value = float(curr['price_usd']) * float(config[curr['symbol']])
            print("{0:6} {1:6}: {2:.2f} USD".format(config[curr['symbol']], curr['symbol'], value))
            sum += value
        print("total balance = {0:.2f} USD".format(sum))
else:
    print("usage: python " + sys.argv[0] + " config.json")
