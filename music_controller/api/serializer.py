from rest_framework import serializers
from  . models import Room
class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields=('id','code','host','guest_can_pause','votes_to_skip','cretated_at')

