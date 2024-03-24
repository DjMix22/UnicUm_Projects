import requests
from time import strftime, localtime


def get_price():
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    block = requests.get(url).json()
    price = "%.2f" % float(block["price"])
    return price


def get_time():
    time = strftime('%H:%M:%S', localtime())
    return time


def main():
    time = get_time()
    price = get_price()
    return [time, price]
