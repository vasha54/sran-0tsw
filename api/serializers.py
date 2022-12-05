from rest_framework import serializers
from touristresource.models import TouristResource, TouristResourceImage

class TouristResourceImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = TouristResourceImage
        fields = ['name', 'description', 'image']

class TouristResourceSerializers(serializers.ModelSerializer):
    
    images = TouristResourceImageSerializers(many=True,read_only=True)
    
    class Meta:
        model = TouristResource  
        exclude = []
        fields = ['id', 'name', 'description','images']
        
    
        
