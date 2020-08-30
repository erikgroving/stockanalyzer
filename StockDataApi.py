import requests

class StockDataApi:
    url_base = 'https://cloud.iexapis.com/'
    ver = 'stable/'
    token = 'pk_64987d421e994d87b1b0b096ab7db3e6'

    def performQuery(self, query):
        r = requests.get(query)
        return r.json()

    def getTickerPriceAndVolumeData(self, ticker, params):
        query = self.createBaseQueryString(ticker)
        query += '/batch/'
        query += self.createParamString(params)
        print(query)
        return self.performQuery(query)
        
    def getRsiData(self, ticker, range, period):
        params = []
        params.append(('range', range))
        params.append(('period', period))
        query = self.createBaseQueryString(ticker) + '/indicator/rsi/'
        query += self.createParamString(params)
        print(query)
        return self.performQuery(query)

    def createBaseQueryString(self, ticker):
        return self.url_base + self.ver + 'stock/' + ticker 
                

    def createParamString(self, params):
        firstParam = True
        paramString = '?'
        params.insert(0, ('token', self.token))
        for [label, value] in params:
            if firstParam != True:
                paramString += '&'
            firstParam = False
            
            paramString += label + '=' + value
        return paramString

