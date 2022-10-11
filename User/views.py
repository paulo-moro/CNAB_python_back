from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from User.models import User
from User.permissions import IsAdminOrOwner
from User.serializer import UserDetailSerializer, UserSerializer

# Create your views here.


class RegisterUserView(generics.CreateAPIView):
    """Create User Api View"""

    serializer_class = UserDetailSerializer


class ListUserView(generics.ListAPIView):
    """List users View"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserProfile(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve Update and destroy view"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminOrOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
