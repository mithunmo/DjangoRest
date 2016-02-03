from rest_framework import serializers
from models import MofilmUser

class MofilmUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MofilmUser
        fields = '__all__'



