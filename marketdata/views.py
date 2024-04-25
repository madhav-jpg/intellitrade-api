from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import ast
from multiprocessing import Pool
from wsdata import WSData
import threading

wsconn = WSData()

@api_view(['POST'])
def startdata(request):
    connect = request.POST.get('connect')
    subscription = request.POST.get('quote')

    thr = threading.Thread(target=wsconn.startWS, args=(connect, subscription), kwargs={})
    thr.start()
    return Response({'message': 'Successful'})

@api_view(['POST'])
def stopdata(request):
    # stopStream()
    return Response({'message': 'Successful'})

@api_view(['POST'])
def fetchdata(request):
    return Response(ast.literal_eval(wsconn.getData()))