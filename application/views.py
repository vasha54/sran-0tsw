from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

from application.forms import LoginForm

from core.settings import NAME_APP,NAME_APP_SHORT

from accescontrol.models import UserDRPA
# Create your views here.

class ViewApp(View):
    template_name = 'page_build.html'
    
    def __init__(self, **kwargs):
        super(ViewApp,self).__init__(**kwargs)
        self.data={}
    
    def dispatch(self,*args,**kwargs):
        return super(ViewApp,self).dispatch(*args,**kwargs)
    
    def getDataInit(self,_request=None):
        dataInit = {
            'nameApp':NAME_APP,
            'nameAppShort' :NAME_APP_SHORT
        }
        
        if _request != None:
            if _request.user != None:
                dataInit['nameCompleted'] = _request.user.nameCompleted()
                dataInit['rol'] = _request.user.getRol()
                dataInit['url_avatar'] = _request.user.logo.url
        
        return dataInit
    
    def get(self, request, *args, **kwargs):
        dataInit = self.getDataInit()
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        dataInit = self.getDataInit()
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)


class LoginView(ViewApp):
    template_name = 'index.html'
    form_class = LoginForm
    
    def dispatch(self,*args,**kwargs):
        return super(LoginView,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.data['form'] =form
        dataInit = self.getDataInit()
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST or None)
        if form.is_valid() == True:
            person = form.getPerson()
            if UserDRPA.objects.existUsserWithAccount(person['username'],person['password']) == False:
               UserDRPA.objects.registerPersonUM(person)
            user = authenticate(username=person['username'],password=person['password'])
            if user is not None:
               if user.is_active:
                   login(request, user)
                   return HttpResponseRedirect('/home',)
            
            self.data = self.getDataInit()
            self.data['form'] =form
            self.data['loginIncorrect']=True
            self.data['errorMessage']='Su cuenta no esta activa. Contacte con los administradores del sistema' 
            return render(request,self.template_name,self.data)
        else:
            self.data = self.getDataInit()
            self.data['form'] =form
            self.data['loginIncorrect']=True
            self.data['errorMessage'] = form.getPerson()['errorMessage']
        return render(request,self.template_name,self.data)
    

class HomeView(ViewApp):
    
    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super(HomeView,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    

class ProfileView(ViewApp):
    
    def dispatch(self,*args,**kwargs):
        return super(ProfileView,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
class ContactView(ViewApp):
    
    def dispatch(self,*args,**kwargs):
        return super(ContactView,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
class ReportView(ViewApp):
    
    def dispatch(self,*args,**kwargs):
        return super(ReportView,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    

class FAQView(ViewApp):
    
    def dispatch(self,*args,**kwargs):
        return super(FAQView,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        return render(request,self.template_name,self.data)
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
    

    
