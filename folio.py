#!/usr/bin/env python
import binance.client
import python_bitbankcc
from sys import exit
import mysetting
import time
import json # for binance
import csv
from datetime import datetime as dt

# Objects and functions -------------------------------
class Object: pass
class Binance:
  def __init__(self, key, secret):
    """
    gets binance information.
    initBinance(key, secret)
    key    = API key    for binance
    secret = API secret for binance
    self.client = client Object
    self.exinfo = exchangeInfo
    self.limit  = limit of access
    self.symbollist = symbol list
    """
    self.client=binance.client.Client(key,secret)
    self.exinfo=self.client.get_exchange_info()
    self.last = time.time()
    self.margin = 2 # margin to access limit
    # get rateLimit
    for e in self.exinfo["rateLimits"]:
      if e["rateLimitType"] == "REQUESTS":
        self.limit=e["limit"]
    self.symbollist=self.exinfo["symbols"] 

  def wait(weight):
    return
  def getprice(t, base, quote):
    return
    

class Bitbank:
  def __init__(self):
    self.pub = python_bitbankcc.public();

def market2base(symbols, market):
  """returns (base, quoite) from symbol.
     symbols = binance symbols list in exchangeInfo"""
  listedsymbol=finddic(symbols, "symbol", market)
  if listedsymbol is not None:
    base =listedsymbol["baseAsset"]
    quote=listedsymbol["quoteAsset"]
    return (base, quote)
  else:
    return (None, None)

def finddic(diclist, key, val):
  """searches the dictionary which has {key0:val0} in the list."""
  #import pdb; pdb.set_trace()
  for dic in diclist:
    if key in dic:
      if dic[key]==val:
        return dic
  return None

# Entry point-------------------------------------------
binance = Binance(mysetting.BINANCE_KEY, mysetting.BINANCE_SECRET)
bitbank = Bitbank()

# analyse binance.csv
with open(mysetting.BINANCE_HIST,'r') as f:
  reader = csv.DictReader(f)
  for row in reader:
    actime = dt.strptime(row["Date"],"%Y-%m-%d %H:%M:%S")
    market = row["Market"]
    (base, quote) = market2base(binance.symbollist, market)
    if row["Type"]=="BUY":
      bought = base
      sold   = quote
    else:
      bought = quote
      sold   = base
    print({"actime":actime,"market":market,"base":base,'quote':quote,'bought':bought,"sold":sold});

exit();

# test binance -------
result=bnClient.get_klines(
  symbol   ="ETHBTC",
  interval =binance.client.Client.KLINE_INTERVAL_1MINUTE,
  limit    =1,
  startTime=int(time.time()*1000-1000*60*10),
)

print(result)

