from django import forms
from touristresource.models import TouristResource, TouristResourceImage

class TouristResourceAddForm(forms.ModelForm):
    
    hasImages = forms.BooleanField(required=False,initial=False,label='Tiene imagen ?')
    
    def __init__(self, *args, **kwargs):
        super(TouristResourceAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] ='form-control'
        self.fields['description'].widget.attrs['class'] ='form-control'
        self.fields['description'].widget.attrs['rows'] = 6
        self.fields['description'].widget.attrs['style'] = 'resize: none;'
        self.fields['hasImages'].widget.attrs['class'] = 'form-check-input'
        
    
    class Meta:
        model = TouristResource
        fields = ['name','description']
        exclude = []

class TouristResourceUpdateForm(TouristResourceAddForm):
    
    def __init__(self, *args, **kwargs):
        super(TouristResourceUpdateForm, self).__init__(*args, **kwargs)
    

class TouristResourceImageAddForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(TouristResourceImageAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] ='form-control'
        self.fields['description'].widget.attrs['class'] ='form-control'
        self.fields['description'].widget.attrs['rows'] = 6
        self.fields['description'].widget.attrs['style'] = 'resize: none;'
    
    
    class Meta:
        model = TouristResourceImage
        fields = ['name','description','image']
        exclude = ['idTouristResource']

class TouristResourceImageUpdateForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super(TouristResourceImageUpdateForm, self).__init__(*args, **kwargs)
    

