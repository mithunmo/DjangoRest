from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets
from serializers import UserSerializer
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework import status
from submodel.model1 import MandrillParam

import mandrill

#class UserViewSet(viewsets.ReadOnlyModelViewSet):
class UserViewSet(viewsets.ModelViewSet):

    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    print "reset"

    @list_route(methods=['GET'])
    def resetPassword(self, request):
        print "sd"
        #u = User.objects.get(email__exact='it@mofilm.com')
        u = User.objects.get(email='it@mofilm.com')
        print u.username
        #u.set_password('password')
        #u.save()

        try:
            mandrill_client = mandrill.Mandrill('xxxxx')
            mandrillObj = MandrillParam("xxxx", "ddd", 'dddd', 'ddddd', 'ddd', 'xxxx', "xxx" )
            message = mandrillObj.getMandrillMessage()
            result = mandrill_client.messages.send(message=message, async=False)

        except mandrill.Error, e:
            # Mandrill errors are thrown as exceptions
            print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
            # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
            raise
        return Response(status.HTTP_200_OK)
