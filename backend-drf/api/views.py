from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StockPredictionSerializer
from rest_framework.response import Response
from rest_framework import status
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
from django.conf import settings

class StockPredictionAPIView(APIView):
    def post(self, request):
        serializer = StockPredictionSerializer(data=request.data)
        if serializer.is_valid():
            ticker = serializer.validated_data['ticker']

            # Fetch the data from yfinance
            now = datetime.now()
            start = datetime(now.year - 10, now.month, now.day)
            end = now
            df = yf.download(ticker, start, end)
            if df.empty:
                return Response({'error': 'No data found for the given ticker.',
                                 'status': status.HTTP_404_NOT_FOUND})
            df = df.reset_index()

            # Generate Basic Plot
            plt.switch_backend('AGG')
            plt.figure(figsize=(12, 5))
            plt.plot(df.Close, label='Closing Price')
            plt.title(f'Closing Price of {ticker}')
            plt.xlabel('Date')
            plt.ylabel('Close Price')
            plt.legend()

            # Save the plot to a file
            plot_img_path = f'{ticker}_plot.png'
            image_path = os.path.join(settings.MEDIA_ROOT, plot_img_path)
            plt.savefig(image_path)
            plt.close()
            image_url = settings.MEDIA_URL + plot_img_path
            print(image_url)
            

            return Response({'status': 'success', 'ticker': ticker})