from rest_framework.response import Response
from rest_framework.decorators import api_view
from projectBase.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    #person = {'name':'Scott','age':28}
    #return Response(person)

    return Response(serializer.data)