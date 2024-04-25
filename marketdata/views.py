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
    global wsconn
    thr = threading.Thread(target=wsconn.startWS, args=(connect, subscription), kwargs={})
    thr.start()
    return Response({'message': 'Successful'})

@api_view(['POST'])
def stopdata(request):
    # stopStream()
    return Response({'message': 'Successful'})

@api_view(['GET'])
def getdata(request):
    global wsconn
    return Response(ast.literal_eval(wsconn.getData()))





# import base64
# from django.shortcuts import render
# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import ast
# from multiprocessing import Pool
# from wsdata import WSData
# import threading
# import pickle

# @api_view(['POST'])
# def startdata(request):
#     connect = request.POST.get('connect')
#     subscription = request.POST.get('quote')
#     wsconn = WSData()
#     thr = threading.Thread(target=wsconn.startWS, args=(connect, subscription), kwargs={})
#     thr.start()
#     pkstr = pickle.dumps(wsconn)
#     # print(pkstr)
#     encoded_data = base64.b64encode(pkstr).decode('utf-8')
#     # print(encoded_data)
#     # print(base64.b64decode(encoded_data.encode('utf-8')))
#     request.session['wsconn'] = encoded_data
#     return Response({'message': 'Successful'})

# @api_view(['POST'])
# def stopdata(request):
#     # stopStream()
#     return Response({'message': 'Successful'})

# @api_view(['GET'])
# def getdata(request):
#     encoded_data = request.session['wsconn']
#     pkstr = base64.b64decode(encoded_data.encode('utf-8'))
#     wsconn = pickle.loads(pkstr)
#     return Response(wsconn.getData())