from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework import permissions

#from quickstart.permissions import IsOwnerOrReadOnly

from models import Movie
from rest_framework import viewsets
from serializers import MoviesSerializer
from serializers import MoviesDetailSerializer
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from pprint import pprint
from rest_framework import status

from django.shortcuts import get_object_or_404

class MoviesViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('status', 'userID','avgRating',)
    permission_classes = (AllowAny, IsAuthenticatedOrReadOnly, )

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MoviesDetailSerializer(user)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def movieList(self, request):
	print "mm"
        recent_users = Movie.objects.all()
        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

    @detail_route(methods=['POST'])
    def set_password(self, request, pk=None):
        print "sss"

    @list_route(methods=['post'])
    def movie_save(self, request, pk=None):
        print request.data
        #pprint (vars(request))
        #print request
        print "sss"
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            print "valid"
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            print serializer.errors
            return Response(status=status.HTTP_400_BAD_REQUEST)




        #user = self.get_object()
        #serializer = PasswordSerializer(data=request.data)
        #if serializer.is_valid():
           # user.set_password(serializer.data['password'])
            #user.save()
            #return Response({'status': 'password set'})
        #else:
          #  return Response(serializer.errors,
           #                 status=status.HTTP_400_BAD_REQUEST)

    #@detail_route(methods=['post'], permission_classes=[IsAuthenticated])
    #def set_password(self, request, pk=None):
    #    print "ms"

