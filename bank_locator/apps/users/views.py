"""User views"""
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from .models import CustomUserModel
from .serializers import TokenSerializer, UserSerializer


class LoginView(generics.CreateAPIView):
    """Login user"""
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUserModel.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # login saves the user’s ID in the session,
        # using Django’s session framework.
        login(request, user)

        serializer = TokenSerializer(
            data={
                'token': api_settings.JWT_ENCODE_HANDLER(api_settings.JWT_PAYLOAD_HANDLER(user))
            }
        )
        serializer.is_valid()

        return Response(serializer.data)


class CreateUserView(generics.CreateAPIView):
    """Register user"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        """Creates user"""
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            if user:
                return Response({'detail': 'ok'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
