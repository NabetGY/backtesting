import requests
import csv
from celery import shared_task


from ticker.models import Ticker

@shared_task
def add(x, y):
    return x + y

@shared_task
def hola():
    print('Hola gente...')

@shared_task
def get_info_ticker():

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    try:
        r = requests.get(url)
    except requests.ConnectionError as e:
        raise Exception("Failed operation...", e)

    if r.status_code in [200, 201]:
        data = r.json()
        print(data.get("Meta Data"))


def get_tickers():
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    CSV_URL = 'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=ZZEAYA9XZ9SNIFGT'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            if row[2]=='NYSE':
                symbol = row[0]
                name = row[1]
                print(symbol)
                Ticker.objects.create(name=name, symbol=symbol)
