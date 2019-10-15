import urllib.request
API_KEY = 'WA7C3UOYSO7QCPGD'  

def getStockData(symbol):
    baseURL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols='
    ending = '&apikey=' + API_KEY
    fullURL = baseURL + symbol + ending
    print()
    print('Sending URL:', fullURL)
    
    connection = urllib.request.urlopen(fullURL)
    
    responseString = connection.read().decode()
    print('Response is: ', responseString)
    
    prefixString = '"2. price": "'
    
    prefixStringPosition = responseString.index(prefixString)
    prefixStringLength = len(prefixString)
    start = prefixStringPosition + prefixStringLength
    end = responseString.index('"', start)
    
    price = responseString[start:end]
    return price
while True:
    print()
    userSymbol = input('Enter a stock symbol (or press ENTER to quit): ')
    if userSymbol == '':
        break
    thisStockPrice = getStockData(userSymbol)
    print()
    print('The current price of', userSymbol, 'is:', thisStockPrice)
    print()
print('BYE')
