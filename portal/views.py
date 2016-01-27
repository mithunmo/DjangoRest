from django.shortcuts import render
from models import PortalProject
from models import Portal
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework.response import Response
from pprint import pprint
from rest_framework import status




# Create your views here.

from serializers import PortalProjectSerializer
from serializers import PortalSerializer

class PortalViewSet(viewsets.ModelViewSet):
    queryset = Portal.objects.all()
    serializer_class = PortalSerializer
    print "outside func ====  222"

    @detail_route(methods=['post','get'])
    def portalProject(self, request, pk=None):
        print "in here"
        if request.method == 'POST':
            print "in post"
            request.data["projectID"] = 3
            serializerProject = PortalProjectSerializer(data=request.data)
            serializerPortal = PortalSerializer(data=request.data)
            if serializerPortal.is_valid():
                portalObject = serializerPortal.save()
                request.data["portalID"] = portalObject.id
                if serializerProject.is_valid():
                    serializerProject.save()
                else:
                    print serializerProject.errors
                return Response(status=status.HTTP_200_OK)
            else:
                print serializerPortal.errors
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            print "in get" + request.method
            #pprint (vars(request))
            return Response(status=status.HTTP_200_OK)


    @detail_route(methods=['get'])
    def project(self, request, pk=None):
        print "dasd"
        return Response(status=status.HTTP_200_OK)



class PortalProjectViewSet(viewsets.ModelViewSet):
    queryset = PortalProject.objects.all()
    serializer_class = PortalProjectSerializer

    print "ssa"
