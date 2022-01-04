from django.shortcuts import render
from rest_framework.generics import GenericAPIView
# Create your views here.

class RegisterAPIView( GenericAPIView ):
    
    def post(self, request ):
        pass