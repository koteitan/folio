#!/usr/bin/env python
import binance.client
import python_bitbankcc
from sys import exit
import mysetting
import time
import json # for binance
import csv

bnClient=binance.client.Client(mysetting.BINANCE_KEY, mysetting.BINANCE_SECRET);
result=bnClient.get_exchange_info();
#import pdb; pdb.set_trace()
for e in result["rateLimits"]:
  if e["rateLimitType"] == "REQUESTS":
    accesslimit=e["limit"]
print accesslimit
exit();



with open(mysetting.BINANCE_HIST,'r') as f:
  reader = csv.reader(f)
  header = next(reader)
  for row in reader:
    print row

# test bitbank -------
bbClient=python_bitbankcc.public();
value=bbClient.get_candlestick('btc_jpy','1min','20180101');
print(value);

# test binance -------
result=bnClient.get_klines(
  symbol   ="ETHBTC",
  interval =binance.client.Client.KLINE_INTERVAL_1MINUTE,
  limit    =1,
  startTime=int(time.time()*1000-1000*60*10),
)

print(result)

