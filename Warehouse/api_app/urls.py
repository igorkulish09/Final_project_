from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from django.urls import path, include
from .views import APIResponseView
from . import views

router = DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/', APIResponseView.as_view(), name='api_response'),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('add_book/', views.add_book, name='add_book'),
]

