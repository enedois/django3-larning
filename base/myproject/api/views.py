from rest_framework.response import Response
from rest_framework.decorators import api_view
from projectBase.models import Item
from .serializers import ItemSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    #person = {'name':'Scott','age':28}
    #return Response(person)

    return Response(serializer.data)

#gets the information
@api_view(['GET'])
def item_detail(request,pk):
    items = Item.objects.filter(pk=pk)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def postData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

##updates the information
@api_view(['PUT'])
def updateData(request,pk):
    items = Item.objects.filter(pk=pk).first()
    serializer = ItemSerializer(items, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request,pk):
    items = Item.objects.get(pk=pk)
    items.delete()
    return Response()       