from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from books.serializers import BookSerializer
from books.models import Book


# all books
class BookAllView(ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('author', 'title', 'desc', 'fandoms', 'category', 'genre')


# my books
class BookMyView(ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('author', 'title', 'desc', 'fandoms', 'category', 'genre')

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)


# 10 random books
class BookRandomView(ListAPIView):
    queryset = Book.objects.all().order_by('fandoms_id')[:10]
    serializer_class = BookSerializer
