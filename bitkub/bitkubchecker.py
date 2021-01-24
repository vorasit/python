 #bitkubchecker.py

import requests
from pprint import pprint
import time

API_HOST = 'https://api.bitkub.com'

mycoin = ['THB_BTC','THB_ETH','THB_DOGE','THB_BCH']

while True:
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    #pprint(result['THB_BTC'])
    for c in mycoin:
        #sym = 'THB_BTC'
        sym = c
        data = result[sym]
        last = data['last']
        #print(data)
        print(sym, last)
    print('-----')
    time.sleep(1)