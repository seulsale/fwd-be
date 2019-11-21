from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics, status
from rest_framework.response import Response


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
        return Note.objects.filter(user=username)
    
    def post(self, request, username):
        request.data['user'] = username
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
