from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.response import Response 
from .models import StockList
from .serializers import StockListSerializer

# Create a new stock list and get all the stock lists that exist
class StockListCreate(generics.ListAPIView):
    queryset = StockList.objects.all()  # Get all StockList objects
    serializer_class = StockListSerializer

    def delete(self, request, *args, **kwargs):
        StockList.objects.all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StockListPostRetrieveUpdateDelete(generics.RetrieveDestroyAPIView):
    queryset = StockList.objects.all()
    serializer_class = StockListSerializer
    lookup_field= "pk" # Primary Key   

