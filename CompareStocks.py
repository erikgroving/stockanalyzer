from StockData import StockData
import matplotlib.pyplot as plt
import numpy as np
import sys

title = ''
nDays = int(sys.argv[1])
nDaysBeforeEnd = int(sys.argv[2])

for arg in sys.argv[3:]:
    dataHandle = StockData(arg)
    dates, changes, closes = dataHandle.getStockData()

    start = len(closes) - nDays
    end = len(closes) - nDaysBeforeEnd 

    data = closes[start:end]
    normData = []
    normData = np.divide(data, data[0])
    normData = normData - normData[0] + 1

    plt.plot(dates[start:end], normData, label=arg)
    title += arg + ' vs '

title = title[:-4] + ' max normalized closes over time'

plt.hlines(1, 0, len(normData) - 1)
plt.xticks(rotation='vertical')
plt.title(title)
plt.xlabel('Date')
plt.legend()
plt.grid()
plt.show()