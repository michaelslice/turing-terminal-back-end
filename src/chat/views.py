from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')