from binance.client import Client
from sys import exit
import mykey
import time

client=Client(mykey.KEY, mykey.SECRET);
result=client.get_klines(
  symbol   ="ETHBTC",
  interval =Client.KLINE_INTERVAL_1MINUTE,
#  limit    =1,
#  startTime=int(time.time()*1000),
#  endTime  =int(time.time()*1000)
)

print(result)

