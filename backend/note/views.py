import random
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema

from .serializers import NoteSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Note, Tag
from .swagger import create_note, retrieve_note, list_notes, update_note, destroy_note, create_tag, list_tags


class CreateListRetrieveNoteView(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    @swagger_auto_schema(
        request_body=create_note["request_body"],
        operation_description=create_note["description"],
        responses=create_note["responses"],
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description=retrieve_note["description"],
        responses=retrieve_note["responses"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description=list_notes["description"],
        responses=list_notes["responses"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UpdateNoteView(GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    @swagger_auto_schema(
        request_body=update_note["request_body"],
        operation_description=update_note["description"],
        responses=update_note["responses"],
    )
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DestroyNoteView(GenericViewSet, mixins.DestroyModelMixin):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    @swagger_auto_schema(
        operation_description=destroy_note["description"],
        responses=destroy_note["responses"],
    )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Note deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class CreateListTagView(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tag.objects.filter(author=user)

    @swagger_auto_schema(
        operation_description=list_tags["description"],
        responses=list_tags["responses"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=create_tag["request_body"],
        operation_description=create_tag["description"],
        responses=create_tag["responses"],
    )
    def create(self, request, *args, **kwargs):
        # Assign a random color if 'color' is not provided
        if not request.data.get('color'):
            request.data['color'] = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
