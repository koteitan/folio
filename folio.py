import binance.client
import python_bitbankcc
from sys import exit
import mysetting
import time
import json # for binance

# test bitbank -------
bbcl=python_bitbankcc.public();
value=bbcl.get_candlestick('btc_jpy','1min','20180101');
print(value);
exit();

# test binance -------
bncl=binance.client.Client(mysetting.BINANCE_KEY, mysetting.BINANCE_SECRET);
result=bncl.get_klines(
  symbol   ="ETHBTC",
  interval =binance.client.Client.KLINE_INTERVAL_1MINUTE,
  limit    =1,
  startTime=int(time.time()*1000-1000*60*10),
)

print(result)

