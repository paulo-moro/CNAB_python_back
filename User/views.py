from django.shortcuts import render
from rest_framework import generics

from User.models import User
from User.permissions import IsAdminOrOwner
from User.serializer import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# Create your views here.


class ListUserView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    """List users View"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserProfile(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminOrOwner]
