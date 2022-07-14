from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Parking
enter = False

@api_view(['POST'])
def getData(request):
    idx = 1
    print(request.data)
    print(request.data['isParked'])
    for i in request.data['isParked']:
        park = Parking.objects.get(location=idx)
        if i:
            park.isParked = True
        else:
            park.isParked = False
        park.save()
        idx += 1
    prPark = Parking.objects.all()
    for i in prPark:
        print(i.isParked)
    return Response("성공")
@api_view(['GET'])
def sendData(request):
    park = Parking.objects.all()
    isparked = []
    for i in park:
        isparked.append(i.isParked)
    return Response(isparked)
@api_view(['POST'])
def isEnteredE(request):
    enter = request.data['enter']
    return Response("성공")

@api_view(['GET'])
def isEnteredW(request):
    return Response(enter)