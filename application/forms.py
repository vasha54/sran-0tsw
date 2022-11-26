from django import forms

from core.ldapUM import LDAPUM
from accescontrol.models import UserDRPA

class LoginForm(forms.Form):
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput)
   
   def __init__(self, *arg,**kwargs):
      super(LoginForm, self).__init__(*arg,**kwargs)
      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['password'].widget.attrs['class'] = 'form-control'
      self.personsLDAPUM = None
      
   def is_valid(self):
      valid = super(LoginForm,self).is_valid()
      if valid == True:
         username = self.cleaned_data['username']
         password = self.cleaned_data['password']
         #ldapUM = LDAPUM()
         #loginUM = ldapUM.autenticatePersonUM(username,password)
         loginManual = UserDRPA.objects.existUsserWithAccountManual(username,password)
         
         #self.personsLDAPUM = ldapUM.getPerson()
         
         if self.personsLDAPUM == None:
            self.personsLDAPUM ={}
         
         self.personsLDAPUM['username']=username
         self.personsLDAPUM['password']=password
         
         # if loginUM == True:
         #    self.personsLDAPUM['typeAccount']='ldap'     
         #    return True
         
         # el
         if loginManual == True:
            self.personsLDAPUM['typeAccount']='manual'
            return True   
      return True
   
   def getPerson(self):
      return self.personsLDAPUM
