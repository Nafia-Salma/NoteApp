from rest_framework import serializers
from .models import Note, Tag

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "author", "tags", "created_at", "updated_at"]
        # allowing it to be viewed but not modified
        extra_kwargs = {"author": {"read_only": True}}

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', "color", "author"]
        # allowing it to be viewed but not modified
        extra_kwargs = {"author": {"read_only": True}}
