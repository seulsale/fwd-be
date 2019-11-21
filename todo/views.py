from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer


class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class Notas(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        print(username)
        queryset = Note.objects.filter(user=username)
        return queryset
