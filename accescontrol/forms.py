from django import forms
from accescontrol.models import UserDRPA

class AddUserAccesControlForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AddUserAccesControlForm, self).__init__(*args, **kwargs)
        self.fields['password']=forms.CharField(widget=forms.PasswordInput)
        self.fields['first_name'].widget.attrs['class'] ='form-control'
        self.fields['last_name'].widget.attrs['class'] ='form-control'
        self.fields['email'].widget.attrs['class'] ='form-control'
        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['logo'].widget.attrs['class'] ='form-control'
        self.fields['numberPhone'].widget.attrs['class'] ='form-control'
        self.fields['numberMobile'].widget.attrs['class'] ='form-control'
        self.fields['typeAccount'].widget.attrs['class'] ='form-select'
        self.fields['password'].widget.attrs['class'] ='form-control'
        
    class Meta:
        model = UserDRPA
        fields = ['numberPhone','numberMobile','typeAccount','logo','first_name','username','last_name','email','password']
        exclude = ['is_active']
            

class UpdateUserAccesControlForm(AddUserAccesControlForm):
    
    def __init__(self, *args, **kwargs):
        super(UpdateUserAccesControlForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['first_name'].widget.attrs['class'] ='form-control'
        self.fields['last_name'].widget.attrs['class'] ='form-control'
        self.fields['email'].widget.attrs['class'] ='form-control'
        self.fields['username'].widget.attrs['class'] ='form-control'
        self.fields['logo'].widget.attrs['class'] ='form-control'
        self.fields['numberPhone'].widget.attrs['class'] ='form-control'
        self.fields['numberMobile'].widget.attrs['class'] ='form-control'
        self.fields['typeAccount'].widget.attrs['class'] ='form-select'
        
    class Meta:
        fields = ['numberPhone','numberMobile','typeAccount','logo','first_name','username','last_name','email']
        exclude = ['password','is_active']
        
            

        

    