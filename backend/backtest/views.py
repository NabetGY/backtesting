
import json
from django.shortcuts import render
from rest_framework import status

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from backtest.strategies.backtesting import backtest

from backtest.serializers import BacktestSerializer
from ticker.serializers import TickerSerializer, TimeSeriesSerializer


class BacktestViewSet( viewsets.ModelViewSet ):
    serializer_class = BacktestSerializer
    queryset = BacktestSerializer.Meta.model.objects.all()



class BackTestAPIView( APIView ):

    def post( self, request):
        print( request.data )

        resumen, report, timeSerie= backtest( 
            request.data["ticker"], 
            request.data["capital"], request.data["dateStart"], 
            request.data["dateEnd"], request.data["indicatorsData"]
        )
        
        timeSerieSerializer = TimeSeriesSerializer(timeSerie, many=True)
        data = {
            "resumen": resumen,
            "report": report,
            "data": timeSerieSerializer.data
        }
        
        return Response(
                { 
                    'message': 'llegaron los datos',
                    "data": data
                },
                status = status.HTTP_200_OK
            )