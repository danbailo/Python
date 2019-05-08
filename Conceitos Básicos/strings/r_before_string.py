apiKey = "999999"

baseURL = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
baseURL_2 = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

inputURL = baseURL + "&from_currency=" + "BRL" + "&to_currency=" + "USD" + "&apikey=" + apiKey
inputURL_2 = baseURL_2 + "&from_currency=" + "BRL" + "&to_currency=" + "USD" + "&apikey=" + apiKey

print(inputURL)
print(inputURL_2)

print(inputURL == inputURL_2)

print(len(inputURL))
print(len(inputURL_2))