from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ListUsersView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Require authentication to access this view

    def get_queryset(self):
        # Allow listing all users only if the authenticated user is a superuser
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.none()  # Return an empty queryset if not superuser

    def list(self, request, *args, **kwargs):
        # Check if user is superuser before listing users
        if not request.user.is_superuser:
            return Response(
                {'detail': 'Permission denied: only superusers can view all users.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().list(request, *args, **kwargs)
