from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework import permissions


#from models import movies
#from submodels import clientdata
from submodel.model1 import clientdata

from rest_framework import viewsets
from serializers import ClientSerializer
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from pprint import pprint
from rest_framework import status



class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = clientdata.objects.all()
    serializer_class = ClientSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('status', 'userID','avgRating')
    #permission_classes = (AllowAny, IsAuthenticatedOrReadOnly, )
