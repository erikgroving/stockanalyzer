## Requirements:
Install pip3 to get all dependencies

`sudo apt install python3-pip`

`pip3 install matplotlib`

`pip3 install numpy`

`pip3 install requests`

## Usage:
`python3 CompareStocks.py NUMDAYS_BEFORE_START NUMDAYS_BEFORE_END #TICKER_1 #TICKER_2 ... #TICKER_N`

## Notes:
Modify the 'range' parameter in StockDataFetcher.py to set how much data we should fetch from API. Options are:
* '5d' 
* '1m'
* '3m'
* '6m'
* '1y'
* '2y'
* '5y'
* 'max' 

Note that the more data you fetch, the more API messages you use.

If you need to switch the API token, modify the token in StockDataApi.py

## Example
This compares the last 30 days for AAPL, MSFT, and SPY

`python3 CompareStocks.py 30 0 AAPL MSFT SPY`

### Output:
![SPY, AAPL, and MSFT](https://github.com/erikgroving/stock_predictor/blob/master/example.PNG?raw=true)