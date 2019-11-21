from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('user', 'text', 'color')
