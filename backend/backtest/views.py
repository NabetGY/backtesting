
from django.shortcuts import render
from rest_framework import status

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from backtest.serializers import BacktestSerializer


class BacktestViewSet( viewsets.ModelViewSet ):
    serializer_class = BacktestSerializer
    queryset = BacktestSerializer.Meta.model.objects.all()



class BackTestAPIView( APIView ):

    def post( self, request):
        print( request.data )
        
        return Response(
                { 'message': 'llegaron los datos'},
                status = status.HTTP_200_OK
            )