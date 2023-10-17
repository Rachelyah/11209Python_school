import csv

def csv_data():
    with open('yf_2330.csv') as data:
        data = csv.DictReader(data)
        for row in data: 
            Date = row['Date']
            Open = row['Open']
            High = row['High']
            Low = row['Low']
            Close = row['Close']
            Adj_Close = row['Adj Close']
            Volume = row['Volume']
        csv_data = (Date, Open, High, Low, Close, Adj_Close, Volume)

    return  csv_data