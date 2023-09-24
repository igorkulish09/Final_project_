from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from django.shortcuts import render, redirect
from .forms import BookForm
from rest_framework.views import APIView
from rest_framework.response import Response


class APIResponseView(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = BookForm()
    return render(request, 'api_app/add_book.html', {'form': form})
