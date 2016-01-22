from rest_framework import serializers
from models import Movie
from models import Source
from models import Event

"""
class MovieSourcesSerializer(serializers.ModelSerializer):
        class Meta:
            model = movieSources

    	fields = ('movieID', 'sourceID')


class MoviesSerializer(serializers.ModelSerializer):

    #movieSources = serializers.StringRelatedField(many=True)

    #sourceID = serializers.IntegerField(source='sourcesMovie.sourceID')

    sourceID = serializers.IntegerField(source='movieSources.sourceID')

    #movieSources = MovieSourcesSerializer(read_only=True)

    class Meta:
        model = movies

	fields = ('id','shortDesc', 'longDesc','userID','uploaded','modified','credits','active',
                  'status','avgRating','ratingCount','runtime','moderatorID','moderatorComments',
              'private','productionYear', 'moderated', 'sourceID')
"""

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

    class Meta:
        model = Movie
        fields = ('id','shortDesc', 'longDesc','userID','uploaded','modified','credits','active',
                  'status','avgRating','ratingCount','runtime','moderatorID','moderatorComments',
              'private','productionYear', 'moderated', 'sources')



