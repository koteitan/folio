# folio

private cryotofolio manager

## tasks
* access to candles via binance and bitbank API (done)
* access to trade logs (now)
* calculate gains
* server service

## requirements
* python
* binance.client lib to get latest prices
* python_bitbankcc lib to get BTC/JPY
* Binance account and its API key and API secrets
```python:mysetting.py
BINANCE_HIST  ="binance.csv"
BINANCE_KEY   ="(KEY)"
BINANCE_SECRET="(SECRET)"
BITBANK_KEY   ="(KEY)"
BITBANK_SECRET="(SECRET)"
```
* Binance trade history saved as csv from exported xlsx

## install
```
sudo pip install python-binance
sudo pip install git+https://github.com/bitbankinc/python-bitbankcc.git
```

If they don't work please try:
```
sudo apt install python-pip
sudo apt install python-pip --fix-missing
```

```
sudo -H pip install git+https://github.com/bitbankinc/python-bitbankcc.git
```
