from django import forms
from django.core.exceptions import ValidationError
from touristresource.models import TourismType
from core import util

class TourismTypeForm(forms.ModelForm):
    
    def __init__(self,*arg,**kwargs):
        super(TourismTypeForm,self).__init__(*arg,**kwargs)
        
    
    class Meta:
        model = TourismType
        fields = ['type', 'description']
        exclude = ['idTP','slug']
        
    def clean_type_es(self):
        val = self.cleaned_data['type_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = TourismType.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = TourismType.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El tipo de turismo es similar a uno ya existente")
        return val
    
    
    
    
        

        