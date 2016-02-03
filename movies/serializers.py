from rest_framework import serializers
from models import Movie
from models import Source
from models import Event

class EventSerializer(serializers.ModelSerializer):
    #sources = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Event
        fields = ('id','name')


class SourceSerializer(serializers.ModelSerializer):
    #movies = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    events = EventSerializer(read_only=True)

    class Meta:
        model = Source
        #fields = ('id', 'name', 'movies','events')
        fields = ('id', 'name','events')

class MoviesSerializer(serializers.ModelSerializer):
    #sources = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    sources = SourceSerializer(many=True, read_only=True)
    #url = serializers.CharField(source="downloadHD", read_only=True)

    class Meta:
        model = Movie
        fields = ('id','shortDesc', 'longDesc','userID','uploaded','modified','credits','active',
                  'status','avgRating','ratingCount','runtime','moderatorID','moderatorComments',
              'private','productionYear', 'moderated', 'sources', 'url')


class MoviesDetailSerializer(serializers.ModelSerializer):
    #sources = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    sources = SourceSerializer(many=True, read_only=True)
    url = serializers.CharField(source="downloadHD", read_only=True)

    class Meta:
        model = Movie
        fields = ('id','shortDesc', 'longDesc','userID','uploaded','modified','credits','active',
                  'status','avgRating','ratingCount','runtime','moderatorID','moderatorComments',
              'private','productionYear', 'moderated', 'sources', 'url')


