from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets
from serializers import UserSerializer

#class UserViewSet(viewsets.ReadOnlyModelViewSet):
class UserViewSet(viewsets.ModelViewSet):

    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer