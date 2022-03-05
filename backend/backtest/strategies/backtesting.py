import numpy as np
import pandas as pd

from backtest.strategies.MACD import get_MACross
from backtest.strategies.DonchianChannels import get_DonchianChannels

from ticker.models import Ticker, TimeSeries


def get_time_series(symbol, start_date, end_date):

    ticker = Ticker.objects.filter(symbol=symbol).first()
    dateRange = TimeSeries.objects.filter(ticker=ticker,date__range=(start_date, end_date))
    return dateRange.values()


def get_resumen( dateframe ):

    print (dateframe[['date_time','price_in', 'price_out', 'positions', 'profit_loss' ]])

    resumen = {}

    resumen["operations"] = dateframe["profit_loss"].notna().sum()

    resumen["winrate"] = ( np.sum(dateframe["profit_loss"] > 0 ) / resumen['operations'] ) * 100

    resumen["Total_P_L"] = dateframe["profit_loss"].sum()

    resumen["max_profit"] = dateframe["profit_loss"].max()
    
    resumen["max_loss"] = dateframe["profit_loss"].min() if dateframe["profit_loss"].min() < 0 else 0

    return resumen

def get_report( dataframe, capital ):
    sizePosition = capital*0.1
    lossMax = capital*0.01
    stopLoss = lossMax/sizePosition
    target= 2*stopLoss
    print(dataframe.to_string())
    dataframeReport = dataframe.loc[ dataframe['position'] != 0.0, ["position", "date", "buy", "sell"]]

    dataframeReport.columns = ["In_Out", "date_time", "price_in", "price_out"]

    price_out = pd.to_numeric(dataframeReport["price_out"])
    price_in = pd.to_numeric(dataframeReport["price_in"])

    dataframeReport["positions"] = np.where( price_in.notna() , np.floor( sizePosition/price_in), np.floor( sizePosition/price_out) )

    dataframeReport["profit_loss"] = np.where( price_out.notna() , ((price_out-price_in.shift())*dataframeReport["positions"]), np.NaN)

    return dataframeReport


def indicatorFilter( df, data ):

    for item in data:

        if item.get('indicatorName') == 'MACD':
            df = get_MACross( df, item.get('config') )
        
        if item.get('indicatorName') == 'DonchianChannels':
            df = get_DonchianChannels( df, item.get('config') )
        
    return df


def backtest(symbol, capital, start_date, end_date, indicatorData):

    data = get_time_series(symbol, start_date, end_date)
    
    df =  pd.DataFrame(data)

    df = indicatorFilter( df, indicatorData )
    
    df2 = get_report( df, capital )

    resumen = get_resumen(df2)

    df2 = df2.fillna('')

    return resumen, df2.to_dict('tight')