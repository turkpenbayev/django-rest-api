from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Stock
from .serilaizers import StockSerializer

#lists all Stoks al create new one
#stocks/
class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many = True)
        return Response(serializer.data)

    def post(self):
        pass