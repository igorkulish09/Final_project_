from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class APIResponseView(APIView):
    def get(self, request):
        data = {"message": "Hello, API!"}
        return Response(data)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
