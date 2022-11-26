from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect,  JsonResponse, HttpResponse

from application.views import ViewApp
from accescontrol.models import UserDRPA, Role
from accescontrol.forms import UpdateUserAccesControlForm,AddUserAccesControlForm
from core.settings import ITEM_PER_PAGE
from core import util

# Create your views here.
class ListViewAccesControl(ViewApp):
    
    template_name = 'list_accescontrol.html'
    
    def dispatch(self,*args,**kwargs):
        return super(ListViewAccesControl,self).dispatch(*args,**kwargs)
    
    def get(self,request,*args,**kwargs):
        self.data = self.getDataInit(request)
        
        patternSearch = ''
        users = None 
        
        if 'patternSearch' in request.GET.keys():
            patternSearch = request.GET['patternSearch']
            
        listUsers = UserDRPA.objects.searchPattern(patternSearch)
            
        pageSU=request.GET.get('pageSU',1)
        
        paginatoUsers=Paginator(listUsers,ITEM_PER_PAGE)
        
        try:
            pageUser = int(pageSU)
        except PageNotAnInteger:
            pageUser = paginatoUsers.page(1)
        except EmptyPage:
            pageUser = int(paginatoUsers.num_pages)
        
        try:
            users = paginatoUsers.page(pageUser)
        except:
            users = paginatoUsers.page(pageUser-1)
            
        limitPagesWorker=util.limitPagesShow(1,pageUser,paginatoUsers.num_pages)
        
        self.data['patternSearch']=patternSearch
        self.data['users']=users
        self.data['lPLUser']=limitPagesWorker[0]
        self.data['lPRUser']=limitPagesWorker[1]
        
        return render(request,self.template_name,self.data)
    
    def post(self,request,*args,**kwargs):
        self.data = self.getDataInit(request)
        
        patternSearch = ''
        users = None 
        
        if 'patternSearch' in request.POST.keys():
            patternSearch = request.POST['patternSearch']
            
        listUsers = UserDRPA.objects.searchPattern(patternSearch)
            
        pageSU=request.GET.get('pageSU',1)
        
        paginatoUsers=Paginator(listUsers,ITEM_PER_PAGE)
        
        try:
            pageUser = int(pageSU)
        except PageNotAnInteger:
            pageUser = paginatoUsers.page(1)
        except EmptyPage:
            pageUser = int(paginatoUsers.num_pages)
        
        try:
            users = paginatoUsers.page(pageUser)
        except:
            users = paginatoUsers.page(pageUser-1)
            
        limitPagesWorker=util.limitPagesShow(1,pageUser,paginatoUsers.num_pages)
        
        self.data['patternSearch']=patternSearch
        self.data['users']=users
        self.data['lPLUser']=limitPagesWorker[0]
        self.data['lPRUser']=limitPagesWorker[1]
        
        return render(request,self.template_name,self.data)
    
class AddUsserAccesControl(ViewApp):
    
    template_name = 'add_accescontrol.html'
    form_class = AddUserAccesControlForm
    
    def dispatch(self,*args,**kwargs):
        return super(AddUsserAccesControl,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        
        host = request.META['HTTP_HOST']
        referer = request.META['HTTP_REFERER']
        url = referer.split(host)[1]
        
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
        
        self.data['form']= self.form_class()
        self.data['urlBack'] = url
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        
        host = request.META['HTTP_HOST']
        referer = request.META['HTTP_REFERER']
        
        dataInit = self.getDataInit(request)
        for k,v in dataInit.items():
            self.data[k]=v
            
        form = self.form_class(request.POST or None, request.FILES)
        if form.is_valid() == True:
            user=form.save()
            groupUser = Role.objects.get(name=Role.INVITED)
            if groupUser !=None:
                groupUser.user_set.add(user)
            return HttpResponseRedirect(request.POST['urlBack'])
        else:
            self.data['form'] = form
            self.data['urlBack'] = request.POST['urlBack']
            return render(request,self.template_name,self.data)
        

class UpdateUsserAccesControl(ViewApp):
    
    template_name ='update_accescontrol.html'
    form_class = UpdateUserAccesControlForm
    
    def dispatch(self,*args,**kwargs):
        return super(UpdateUsserAccesControl,self).dispatch(*args,**kwargs)
    
    def get(self,request,usuario_id,*args,**kwargs):
        host = request.META['HTTP_HOST']
        referer = request.META['HTTP_REFERER']
        url = referer.split(host)[1]
        try:
            user = UserDRPA.objects.get(username=usuario_id)
            form = self.form_class(instance=user)
            
            self.data=self.getDataInit(request)
            self.data['form'] = form
            self.data['urlBack'] = url 
            self.data['user'] = user
            return render(request,self.template_name,self.data)
        except UserDRPA.DoesNotExist:
            return HttpResponseRedirect(url)
    
    def post(self,request,usuario_id,*args,**kwargs):
        host = request.META['HTTP_HOST']
        referer = request.META['HTTP_REFERER']
        url = referer.split(host)[1]
        try:
            self.data=self.getDataInit(request)
            user = UserDRPA.objects.get(username=usuario_id)
            form = self.form_class(request.POST or None,request.FILES or None,instance=user)
            
            if form.is_valid() == True:
                form.save()
                return HttpResponseRedirect(request.POST['urlBack'])
            else:
                self.data['form'] = form
                self.data['urlBack'] = request.POST['urlBack']
                self.data['user'] = user
                return render(request,self.template_name,self.data) 
        except UserDRPA.DoesNotExist:
            return HttpResponseRedirect(url)
        
    

class DetailsUsserAccesControl(ViewApp):
    
    template_name = 'details_user.html'
    
    def dispatch(self, *args, **kwargs):
        return super(DetailsUsserAccesControl,self).dispatch(*args, **kwargs)
    
    def get(self, request,usuario_id, *args, **kwargs):
        
        host = request.META['HTTP_HOST']
        referer = request.META['HTTP_REFERER']
        url = referer.split(host)[1]
        
        try:
            user = UserDRPA.objects.get(username=usuario_id)
            self.data = self.getDataInit(request)
            self.data['user'] = user
            return render(request, self.template_name,self.data)
        except UserDRPA.DoesNotExist:
            return HttpResponseRedirect(url)
        
    def post(self, request,usuario_id, *args, **kwargs):
        return self.get(request,usuario_id,*args,**kwargs)
    
    
    
def removeUsserAccesControl(request,usuario_id,*arg,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    try:
        user = UserDRPA.objects.get(username=usuario_id)
        if util.canRemoveUserDRPA(user) == True:
            user.delete() 
    except UserDRPA.DoesNotExist:
        pass
    
    return HttpResponseRedirect(url)

def changeStatusUsserAccesControl(request,usuario_id,*arg,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    try:
        user = UserDRPA.objects.get(username=usuario_id)
        user.is_active = False if user.is_active== True else True
        user.save()
    except UserDRPA.DoesNotExist:
        pass
    
    return HttpResponseRedirect(url)
    

def removeRolUsserAccesControl(request,rol,usuario_id,*arg,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    try:
        user = UserDRPA.objects.get(username=usuario_id)
        group = Role.objects.get(name=rol)
        user.groups.remove(group)
    except (UserDRPA.DoesNotExist, Role.DoesNotExist):
        pass
    
    return HttpResponseRedirect(url)


def getDataJSON(_roles):
    data ={}
    if( len(_roles) != 0 ):
        data['succes'] =True
        data['roles'] = _roles
    else:
        data['succes']=False
        data['message']='No existes roles disponibles en el sistema que se le pueda asignar al usuario.'
    return data


def getRolesAviableThisUsserAccesControl(request,usuario_id,*arg,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    if util.is_ajax(request):
        rolesAviables = UserDRPA.objects.listRolesAviablesForThisUser(usuario_id)
        dataJSON = getDataJSON(rolesAviables)
        dataJSON['urlRequest'] = url
        response = JsonResponse(dataJSON)
        return HttpResponse(response.content)
    else:
        return HttpResponseRedirect(url)
    
def addRolesThisUsserAccesControl(request,list_roles,usuario_id,*arg,**kwargs):
    
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    if util.is_ajax(request):
        roles = list_roles.split("@")
        UserDRPA.objects.addRolesThisUser(roles,usuario_id)
    
    return HttpResponseRedirect(url)
    
    
    

