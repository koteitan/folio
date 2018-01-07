# folio

private cryotofolio manager

## tasks
* access candles via binance and bitbank API (done)
* access trade logs (now)
* calculate gains
* server service

## requirements
* python
* binance.client lib to get latest prices
* python_bitbankcc lib to get JPY/BTC

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
