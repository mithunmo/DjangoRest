from rest_framework import serializers
from models import Portal
from models import PortalProject
from models import PortalContent
from models import PortalUser
from movies.models import Movie
from users.serializers import UserSerializer

class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = ('id', 'brandID', 'createDate', 'status')
    """
    def create(self, validated_data):
        print "in create"
        print validated_data
        return Portal
    """
class PortalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalProject
        fields = ('id', 'projectID', 'portalID', 'createDate', 'name')


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','shortDesc', 'longDesc','userID')


class PortalContentSerializer(serializers.ModelSerializer):
    movies = MoviesSerializer(read_only=True)
    url = serializers.CharField(source='someText', read_only=True)

    class Meta:
        model = PortalContent
        fields = ('id','portalID','movies', 'contentType', 'licenseTerms', 'url')



class PortalUserSerializer(serializers.ModelSerializer):
    portalID = PortalSerializer(read_only=True)
    userID = UserSerializer(read_only=True)
    class Meta:
        model = PortalUser
        fields = ("portalID", "userID")
