from django.shortcuts import render
from serializers import MofilmUserSerializer
from models import MofilmUser
from rest_framework import viewsets
from rest_framework import filters


# Create your views here.
class MofilmUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MOFILM User to be viewed or edited.
    """

    queryset = MofilmUser.objects.all()
    serializer_class = MofilmUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)
