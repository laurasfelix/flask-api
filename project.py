import finnhub
import requests
finnhub_client = finnhub.Client(
    api_key="chobfq1r01qmdnlqj6t0chobfq1r01qmdnlqj6tg")  # getting information from api through import and finnhub_client

def carl():
    data_finnhub = finnhub_client.stock_symbols('US')
    listy = []
    for i in range(5):
        dicty = {}
        individual_data = data_finnhub[i]
        dicty[individual_data["description"]] = individual_data["displaySymbol"]
        listy.append(dicty)
    return listy

def build():
    data = {}
    result = carl()
    for i in range(5):
        url = finnhub_client.company_basic_financials(list(result[i].values())[0], 'all')
        if url != [] and 'beta' in url['metric'].keys():
            data[list(result[i].keys())[0]] = {'beta': str(url['metric']['beta']), 'symbol': list(result[i].values())[0]}
    return data