#!/bin/python

import urllib.request
import json
import sys
import time
from functools import reduce
from pymongo import MongoClient


def store_data(data, db_client):
    db = db_client.coin_calc_db
    calc_values = db.calc_values
    inserted_id = calc_values.insert_one(data)
    return inserted_id


def connect_to_mongo():
    db_config = json.load(open("db_config.json"))
    client = MongoClient(db_config['db_host'], db_config['db_port'])
    return client


if len(sys.argv) != 1:
    config = json.load(open(sys.argv[1]))
    with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=0") as f:
        res = f.read()
        json_res = json.loads(res.decode())
    currencies = filter(lambda x: x['symbol'] in config.keys(), json_res)
    timestamp = time.time()
    output = dict()
    output['time'] = timestamp
    output['balances'] = dict()
    output['rates'] = dict()

    for curr in currencies:
        value = float(curr['price_usd']) * float(config[curr['symbol']])
        output['balances'][curr['symbol']] = value
        output['rates'][curr['symbol']] = float(curr['price_usd'])

    output['sums'] = reduce(lambda x, y: x + y, output['balances'].values())
    json_string = json.dumps(output)

    db_client = connect_to_mongo()
    inserted = store_data(json_string, db_client)
    if inserted is not None:
        print(inserted)
        sys.exit()

else:
    print("usage: python " + sys.argv[0] + " config.json")



