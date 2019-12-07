"""User serializers"""
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUserModel


class TokenSerializer(serializers.Serializer):
    """This serializer serializes the token data"""
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=16)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

    class Meta:
        model = CustomUserModel
        fields = ('id', 'email', 'username', 'password')
