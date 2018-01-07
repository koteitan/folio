#!/usr/bin/env python
import binance.client
import python_bitbankcc
from sys import exit
import mysetting
import time
import json # for binance
import csv
from datetime import datetime as dt

# functions -------------------------------
def initBinance(key, secret)
  """gets binance information.
    bn=initBinance(key, secret)
    key    = API key    for binance
    secret = API secret for binance
    bn.client = client Object
    bn.exinfo = exchangeInfo
    bn.limit  = limit of access
    bn.symbollist = symbol list
  """
  bn.client=binance.client.Client(key,secret)
  bn.exinfo=bn.client.get_exchange_info()
  # get rateLimit
  for e in bn.exinfo["rateLimits"]:
    if e["rateLimitType"] == "REQUESTS":
      bn.limit=e["limit"]
  bn.symbollist=result["symbols"] 
  return bn

def initBitbank
  bb.pub = python_bitbankcc.public();

def market2base(symbols, market):
  """returns (base, quoite) from symbol.
     symbols = binance symbols list in exchangeInfo"""
  listedsymbol=finddic(symbols, "market")
  if listedsymbol is not None:
    base =listedsymbol["baseasset"]
    quote=listedsymbol["quoteasset"]
    return (base, quote)
  else:
    return None

def finddic(diclist, key0, val0):
  """searches the dictionary which has {key0:val0} in the list."""
  for dic in diclist:
    if key0 in dic:
      if dic[key0]==val0:
        return dic
  return None

# Entry point-------------------------------------------

bn = initBinance(mysetting.BINANCE_KEY, mysetting.BINANCE_SECRET)
bb = initBitbank()

# analyse binance.csv
with open(mysetting.BINANCE_HIST,'r') as f:
  reader = csv.DictReader(f)
  for row in reader:
    actime = dt.strptime(row["Date"],"%Y/%m/%d %H:%M")
    market = row["Market"]
    (base, quote) = market2base(symbols, market)
    if row["Type"]=="BUY":
      bought = base
      sold   = quote
    else:
      bought = quote
      sold   = base
    print({"actime":actime,"market":market,"base":base,'quote':quote,'bought':bought,"sold":sold}

exit()



# test bitbank -------

# test binance -------
result=bnClient.get_klines(
  symbol   ="ETHBTC",
  interval =binance.client.Client.KLINE_INTERVAL_1MINUTE,
  limit    =1,
  startTime=int(time.time()*1000-1000*60*10),
)

print(result)

