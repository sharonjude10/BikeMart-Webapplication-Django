from rest_framework.response import Response
from rest_framework.decorators import api_view
from bikes.models import Destination
from .serializers import DestSerializer


@api_view(['GET'])
def getData(request):
    items = Destination.objects.all()
    serializer = DestSerializer(items, many=True)
    return Response(serializer.data)
