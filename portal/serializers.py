from rest_framework import serializers
from models import Portal
from models import PortalProject

class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = ('id', 'brandID', 'createDate', 'status', 'token')

    def create(self, validated_data):
        print "in create"
        print validated_data
        return Portal

class PortalProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalProject
        fields = ('id', 'projectID', 'portalID', 'createDate')


"""
class MoviesSerializer(serializers.ModelSerializer):
    #sources = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    sources = SourceSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id','shortDesc', 'longDesc','userID','uploaded','modified','credits','active',
                  'status','avgRating','ratingCount','runtime','moderatorID','moderatorComments',
              'private','productionYear', 'moderated', 'sources')
"""


