from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from rest_framework.response import Response 

# Create your views here.
class ReactView(APIView):
    def get(self, request):
        output = [{"person": output.person, 
                   "type": output.type}
                   for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


def home(request):
    return HttpResponse("TEST")