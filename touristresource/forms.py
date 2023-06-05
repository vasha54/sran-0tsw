from django import forms
from django.core.exceptions import ValidationError
from touristresource.models import TourismType, TouristAttraction, TypeService, Schedule, InfrastructureAccess, ResourceTourist #, ValueTouristic, ScheduleService

from django.contrib.gis.geos import Point

from location_field.forms.plain import PlainLocationField


from django.contrib.gis.geos import Point


from core import util

class TouristAttractionForm(forms.ModelForm):
    
    def __init__(self,*arg,**kwargs):
        super(TouristAttractionForm,self).__init__(*arg,**kwargs)
        
    class Meta:
        model = TouristAttraction
        #fields = ['name', 'description']
        exclude = ['idTP','slug']
        
    def clean_name_es(self):
        val = self.cleaned_data['name_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = TouristAttraction.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = TouristAttraction.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El atractivo turístico es similar a uno ya existente")
        return val
    
class TourismTypeForm(forms.ModelForm):
    
    def __init__(self,*arg,**kwargs):
        super(TourismTypeForm,self).__init__(*arg,**kwargs)
        
    class Meta:
        model = TourismType
        #fields = ['name', 'description']
        exclude = ['idTP','slug']
        
    def clean_name_es(self):
        val = self.cleaned_data['name_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = TourismType.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = TourismType.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El tipo de turismo es similar a uno ya existente")
        return val

class TypeServiceForm(forms.ModelForm):
    
    def __init__(self,*arg,**kwargs):
        super(TypeServiceForm,self).__init__(*arg,**kwargs)
        
    class Meta:
        model = TypeService
        #fields = ['name', 'description']
        exclude = ['idTS','slug']
        
    def clean_name_es(self):
        val = self.cleaned_data['name_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = TourismType.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = TourismType.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El tipo de servicio es similar a uno ya existente")
        return val
    
class ScheduleForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Schedule
        #fields = ['name', 'startTime', 'endTime']
        exclude = ['idSchedule','slug']
        
    def clean_name_es(self):
        val = self.cleaned_data['name_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = Schedule.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = Schedule.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El nombre del horario es similar a uno ya existente")
        return val

class InfrastructureAccessForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(InfrastructureAccessForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = InfrastructureAccess
        #fields = ['name']
        exclude = ['idIA','slug']
        
    def clean_name_es(self):
        val = self.cleaned_data['name_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = InfrastructureAccess.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = InfrastructureAccess.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El nombre de la infraestructura de acceso es similar a uno ya existente")
        return val
    
class ResourceTouristForm(forms.ModelForm):
    location = PlainLocationField(based_fields=['city'],label="Localización geográfica",
                             initial=Point(-49.1607606, -22.2876834))
    hasImages = forms.BooleanField(required=False,initial=False,label='Tiene imagen ?')
    
    def __init__(self, *args, **kwargs):
        super(ResourceTouristForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = ResourceTourist
        #fields = ['name','idMunicipality','comments','address','description']
        exclude = ['idRT','slug','geoLocLat','geoLocLon']
        
    def clean_name_es(self):
        val = self.cleaned_data['name_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = ResourceTourist.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = ResourceTourist.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El nombre del recurso turístico es similar a uno ya existente")
        return val
    
    def clean_location(self):
        val = self.cleaned_data['location']
        return val
    

    
    



# class ValueTouristicForm(forms.ModelForm):
    
#     def __init__(self,*arg,**kwargs):
#         super(ValueTouristicForm,self).__init__(*arg,**kwargs)
        
    
#     class Meta:
#         model = ValueTouristic
#         fields = ['value', 'description']
#         exclude = ['idVT','slug']
        
#     def clean_value_es(self):
#         val = self.cleaned_data['value_es']
#         slugNew = util.generateSLUG(val)
#         exist = False
#         if self.instance != None:
#             exist = ValueTouristic.objects.existThisSLUG(slugNew,self.instance.pk)
#         else:
#             exist = ValueTouristic.objects.existThisSLUG(slugNew)
            
            
#         if exist == True:
#             raise  forms.ValidationError("El valor turístico es similar a uno ya existente")
#         return val
    
    

    

    
    
    
    
    
        

        