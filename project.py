import finnhub
import requests
finnhub_client = finnhub.Client(
    api_key="chobfq1r01qmdnlqj6t0chobfq1r01qmdnlqj6tg")  # getting information from api through import and finnhub_client

data_finnhub = finnhub_client.stock_symbols('US')
def carl():
    listy = []
    for i in data_finnhub:
        listy.append(i["displaySymbol"])
    return listy

def build():
    data = []
    result = carl()
    for i in result:
        url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + i + '&interval=5min&apikey=SWIRCWIP8Z0W6BV'
        r = requests.get(url)
        data.append(r.json())
    return data
