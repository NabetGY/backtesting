from turtle import position
import requests
import csv
from celery import shared_task
from django.core.cache import cache



from ticker.models import Ticker, TimeSeries

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


@shared_task
def update_time_series():

    dataTicker = cache.get_many( ['tickerNow', 'interval', 'position' ])

    print(dataTicker)

    if dataTicker == {}:
        print('entro al if ...')
        tickers = list( Ticker.objects.values_list('symbol') )
        dataTicker['tickerNow'] = tickers[0][0]
        dataTicker['interval'] = '1min'
        dataTicker['position'] = 0
        cache.set( 'tickers', tickers )
        cache.set( 'tickerNow', tickers[0][0] )
        cache.set( 'interval', '1min' )
        cache.set( 'position', 0 )

        
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval={}&outputsize=full&apikey=ZZEAYA9XZ9SNIFGT'.format(
        dataTicker.get('tickerNow'), dataTicker.get('interval')
     )

    print(url)

    try:
        r = requests.get(url)
    except requests.ConnectionError as e:
        print('****************************')
        raise Exception("Failed operation...", e)

    if r.status_code in [200, 201]:
        data = r.json()
        
        if data.get('Note') == None:

            symbol = data.get("Meta Data").get("2. Symbol")
            interval = data.get("Meta Data").get("4. Interval")
            last_refreshed = data.get("Meta Data").get("3. Last Refreshed")[:10]
            timeSerieString = "Time Series ({})".format( dataTicker.get('interval'))
            time_serie = data.get( timeSerieString )
            ticker = Ticker.objects.filter(symbol=symbol).first()
            timeSerie = TimeSeries(ticker = ticker, interval= interval,last_Refreshed = last_refreshed, time_series = time_serie)
            timeSerie.save()
            print('Se recopilo con exito el ticket =', symbol)
            tickers = cache.get('tickers')
            cache.set('position', dataTicker.get('position')+1 )
            cache.set('tickerNow', tickers[ dataTicker.get('position') ][0] )

        else:
            print("limite excedido, gomenazai...")

