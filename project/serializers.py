from rest_framework import serializers
#from models import movies
from submodel.model1 import clientdata
#from models import movieSources
#from models import Sources

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientdata

	fields = ('id','sourceID','shortDesc','name')

