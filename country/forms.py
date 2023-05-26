from django import forms
from django.core.exceptions import ValidationError
from country.models import Province, Municipality
from core import util

class ProvinceForm(forms.ModelForm):
    
    def __init__(self,*arg,**kwargs):
        super(ProvinceForm,self).__init__(*arg,**kwargs)
        
    class Meta:
        model  = Province
        fields = ['name', ]
        exclude = ['idProvince','slug']
        
    def clean_name_es(self):
        val = self.cleaned_data['name_es']
        slugNew = util.generateSLUG(val)
        exist = False
        if self.instance != None:
            exist = Province.objects.existThisSLUG(slugNew,self.instance.pk)
        else:
            exist = Province.objects.existThisSLUG(slugNew)
            
            
        if exist == True:
            raise  forms.ValidationError("El tipo de turismo es similar a uno ya existente")
        return val
    
class MunicipalityForm(forms.ModelForm):
    
    def __init__(self,*arg,**kwargs):
        super(MunicipalityForm,self).__init__(*arg,**kwargs)
        
    class Meta:
        model  = Municipality
        fields = ['name', 'idProvince']
        exclude = ['idMunicipality','slug']
        
    def clean(self):
        cleaned_data = super(MunicipalityForm, self).clean()
        if cleaned_data != None:
            name = cleaned_data.get('name_es')
            province = cleaned_data.get('idProvince')
            if name != None and province != None:
                slugProvince = province.slug
                slugNew = util.generateSLUG(slugProvince+'_'+name)
                exist = False
                if self.instance != None:
                    exist = Municipality.objects.existThisSLUG(slugNew,self.instance.pk)
                else:
                    exist = Municipality.objects.existThisSLUG(slugNew)
                if exist == True:
                    raise  forms.ValidationError("Ya existe un municipio con similar nombre en la misma provincia.") 
        return cleaned_data