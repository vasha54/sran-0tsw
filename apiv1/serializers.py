from rest_framework import serializers
from touristresource.models import ResourceTourist, TouristAttraction,TouristAttractionResourceTourist,TourismType,TourismTypeResourceTourist, Service,Schedule, TypeService, InfrastructureAccessResourceTourist, MediaResourceTourist,MediaImageRT
from country.models import  Municipality, Province

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class MunicipalitySerializer(serializers.ModelSerializer):
    
    idProvince = ProvinceSerializer()
    
    class Meta:
        model = Municipality
        fields = "__all__"

class TouristAttractionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TouristAttraction
        fields = "__all__"

class TouristAttractionResourceTouristSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TouristAttractionResourceTourist
        fields = '__all__'

class TourismTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TourismType
        fields = "__all__"

class TourismTypeResourceTouristSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TourismTypeResourceTourist
        fields = '__all__'
        
class InfrastructureAccessResourceTouristSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InfrastructureAccessResourceTourist
        fields = '__all__'
        
class ScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Schedule
        fields = '__all__'

class TypeServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeService
        fields = '__all__'

class MediaResourceTouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaResourceTourist
        fields = '__all__'

class MediaImageRTSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MediaImageRT
        fields = '__all__'
        


class ServiceSerializer(serializers.ModelSerializer):

    idSchedule = ScheduleSerializer()
    idTypeService = TypeServiceSerializer()    
    class Meta:
        model = Service
        fields = ['idService','idSchedule','idTypeService']

class ResourceTouristSerializer(serializers.ModelSerializer):
    
    idMunicipality  = MunicipalitySerializer()
    services = ServiceSerializer(many=True, read_only=True)
    attractions = TouristAttractionResourceTouristSerializer(many=True, read_only=True)
    infrastructure_access = InfrastructureAccessResourceTouristSerializer(many=True, read_only=True)
    type_tourism = TourismTypeResourceTouristSerializer(many=True, read_only=True)
    medias = MediaResourceTouristSerializer(many=True, read_only=True)
    
    class Meta:
        model = ResourceTourist
        fields = ['name','slug','description','address','comments','geoLocLat','geoLocLon','idMunicipality','services','attractions','infrastructure_access','medias']