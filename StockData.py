import json
import matplotlib.pyplot as plt
import numpy as np
from os import path
from StockDataApi import StockDataApi
from StockDataFetcher import StockDataFetcher

class StockData:

    def __init__(self, ticker):
        self.ticker = ticker
        self.volume = []
        self.dayChanges = []
        self.dates = []
        self.close = []

    def readDataFromJson(self):
        if self.volume:
            return
        filename = self.ticker + '_stockData.json'
        if path.exists(filename) != True:
            fetcher = StockDataFetcher()
            fetcher.writeDataToFile(self.ticker)
        file = open(filename, 'r')
        stockdata = json.load(file)

        for day in stockdata['chart']:
            self.dates.append(day['date'])
            self.volume.append(day['volume'])
            self.close.append(day['close'])
            self.dayChanges.append(day['changePercent'])
        return 

    def getStockData(self):
        self.readDataFromJson()
        return self.dates, self.dayChanges, self.close
