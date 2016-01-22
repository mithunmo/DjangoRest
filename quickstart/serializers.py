from rest_framework import serializers
from models import movies
#from models import movieSources
#from models import Sources

class MoviesSerializer(serializers.ModelSerializer):
    movieSources = serializers.StringRelatedField(many=True)


    #event = serializers.SerializerMethodField('event')
  
    #sources = serializers.StringRelatedField(many=True)
    mm = "ddd"
    #movieSources = serializers.RelatedField(many=True, read_only=`True`)
    #movieSources = serializers.PrimaryKeyRelatedField(read_only=`True`)
    
    class Meta:
        model = movies

	fields = ('id','shortDesc', 'longDesc','userID','uploaded','modified','credits','active',
                  'status','avgRating','ratingCount','runtime','moderatorID','moderatorComments','private','productionYear', 'moderated', 'movieSources')

