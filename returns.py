#!/usr/bin/env python
# coding: utf-8

### IMPORT LIBRARIES ###
import requests


### GET CURRENT BTCUSD AND ETHUSD PRICES FROM COINBASE ###
BTC_PRICE = float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot').json()['data']['amount'])
ETH_PRICE = float(requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot').json()['data']['amount'])


### INPUT TOTAL BTC AND ETH INVESTED ###
CURRENT = {'BTC': BTC_PRICE,
          'ETH': ETH_PRICE}
INVESTED = {'BTC': float(input('Total BTC Invested = ')),
            'ETH': float(input('Total ETH Invested = '))}


### CALCULATE BUY & HOLD VALUE OF BTC AND ETH INVESTMENTS ###
SPOT = {}
for symbol in CURRENT.keys():
    SPOT[symbol] = round(CURRENT[symbol]*INVESTED[symbol], 2)


### INPUT ALL TOKENS HELD ###
TOKENS_HELD = []
print('Enter all tokens held individually\nOr enter DONE to finish\n')
while True:
    TOKEN = input('> ')
    if TOKEN.lower() == 'done':
        break
    else:
        TOKENS_HELD.append(TOKEN)


### INPUT CURRENT TOTAL ETH VALUE OF EACH TOKEN HELD ###
HOLDINGS= {}
for symbol in TOKENS_HELD:
    HOLDINGS[symbol] = round(float(input('Current '+symbol+' ETH Value = '))*ETH_PRICE, 2)
CURRENT_USD = round(sum(HOLDINGS.values()), 2)

SORT_HOLDINGS = sorted(HOLDINGS.items(), key=lambda x: x[1], reverse=True)


### SHOW CURRENT INDIVIDUAL AND TOTAL USD VALUES ###
print('Current USD Values\n')
for items in SORT_HOLDINGS:
    print(items[0]+': '+'$'+str(items[1]))
print('Total: '+'$'+str(CURRENT_USD))


### CALCULATE USD RETURNS OF CURRENT HOLDINGS VS BUY AND HOLD ###
RETURNS = {}
for symbol in CURRENT.keys():
    RETURNS[symbol] = '$'+str(round(CURRENT_USD-SPOT[symbol], 2)) + ' | '+ str(round((CURRENT_USD-SPOT[symbol])/SPOT[symbol]*100, 2))+'%'


### PRINT USD RETURNS OF CURRENT HOLDINGS VS BUY AND HOLD ###
print('Current Returns vs BTC and ETH Spot\n')
for k,v in RETURNS.items():
    print(k+': '+v)

