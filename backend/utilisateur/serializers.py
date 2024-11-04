from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        # only set but not retrieved, security raison.
        extra_kwargs = {"password": {"write_only": True}}
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
