from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect,  JsonResponse, HttpResponse
from django.forms import formset_factory

from application.views import ViewApp
from touristresource.models import TouristResource, TouristResourceImage
from touristresource.forms import TouristResourceAddForm, TouristResourceUpdateForm, TouristResourceImageAddForm, TouristResourceImageUpdateForm
from core.settings import ITEM_PER_PAGE
from core import util

    
    
    
    
class ListViewTouristResource(ViewApp):
    
    template_name = 'list_touristresource.html'
    
    def dispatch(self,*args,**kwargs):
        return super(ListViewTouristResource,self).dispatch(*args,**kwargs)
    
    def get(self, request, *args, **kwargs):
        self.data = self.getDataInit(request)
        
        patternSearch = ''
        touristResources = None 
        
        if 'patternSearch' in request.GET.keys():
            patternSearch = request.GET['patternSearch']
            
        listTouristResource = TouristResource.objects.searchPattern(patternSearch)
            
        pageSU=request.GET.get('pageSU',1)
        
        paginatoTouristResource=Paginator(listTouristResource,ITEM_PER_PAGE)
        
        try:
            pageTouristResource = int(pageSU)
        except PageNotAnInteger:
            pageTouristResource = paginatoTouristResource.page(1)
        except EmptyPage:
            pageTouristResource = int(paginatoTouristResource.num_pages)
        
        try:
            touristResources = paginatoTouristResource.page(pageTouristResource)
        except:
            touristResources = paginatoTouristResource.page(pageTouristResource-1)
            
        limitPagesTouristResource=util.limitPagesShow(1,pageTouristResource,paginatoTouristResource.num_pages)
        
        self.data['patternSearch']=patternSearch
        self.data['touristResources']=touristResources
        self.data['lPLTouristResource']=limitPagesTouristResource[0]
        self.data['lPRTouristResource']=limitPagesTouristResource[1]
        
        return render(request,self.template_name,self.data)
        
    
    def post(self, request, *args, **kwargs):
        self.data = self.getDataInit(request)
        
        patternSearch = ''
        touristResources = None 
        
        if 'patternSearch' in request.POST.keys():
            patternSearch = request.POST['patternSearch']
            
        listTouristResource = TouristResource.objects.searchPattern(patternSearch)
            
        pageSU=request.GET.get('pageSU',1)
        
        paginatoTouristResource=Paginator(listTouristResource,ITEM_PER_PAGE)
        
        try:
            pageTouristResource = int(pageSU)
        except PageNotAnInteger:
            pageTouristResource = paginatoTouristResource.page(1)
        except EmptyPage:
            pageTouristResource = int(paginatoTouristResource.num_pages)
        
        try:
            touristResources = paginatoTouristResource.page(pageTouristResource)
        except:
            touristResources = paginatoTouristResource.page(pageTouristResource-1)
            
        limitPagesTouristResource=util.limitPagesShow(1,pageTouristResource,paginatoTouristResource.num_pages)
        
        self.data['patternSearch']=patternSearch
        self.data['touristResources']=touristResources
        self.data['lPLTouristResource']=limitPagesTouristResource[0]
        self.data['lPRTouristResource']=limitPagesTouristResource[1]
        
        return render(request,self.template_name,self.data)
    
class AddTouristResource(ViewApp):
    
    template_name = 'add_touristresource.html'
    form_class = TouristResourceAddForm
    
    def dispatch(self, request, *args, **kwargs):
        return super(AddTouristResource,self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        host = request.META['HTTP_HOST']
        referer = request.META['HTTP_REFERER']
        url = referer.split(host)[1]
        
        self.data = self.getDataInit(request)
        self.data['form'] = self.form_class()
        self.data['urlBack'] = url
        
        
        MultipleFormSetTouristResourceImage = formset_factory(TouristResourceImageAddForm,formset=util.RequeridFormSet,extra=1,max_num=5, can_delete=True)
        formMultipleImageTR = MultipleFormSetTouristResourceImage()
        
        self.data['formMultipleImageTR'] = formMultipleImageTR
        
        return render(request,self.template_name,self.data)
    
    def post(self, request, *args, **kwargs):
        
        self.data = self.getDataInit(request)
        
        formResource = self.form_class(request.POST or None, request.FILES)
        MultipleFormSetTouristResourceImage = formset_factory(TouristResourceImageAddForm,formset=util.RequeridFormSet,can_delete=True)
        formMultipleImageTR = MultipleFormSetTouristResourceImage(request.POST or None, request.FILES)
        
        validFResource = formResource.is_valid()
        validFAllImage = True
        
        dataMultipleFormImage = []
        formErrors = []
        
        hasImage=formResource.cleaned_data['hasImages']
        
        if hasImage == True:
            for form in formMultipleImageTR:
                if form.is_valid() == True:
                    fill = {'description':form.cleaned_data['description'],
                        'name':form.cleaned_data['name'],
                        'image':form.cleaned_data['image'],}
                    dataMultipleFormImage.append(fill)
                else:
                    blank = {'description':'',
                             'name':'',
                             'image':'',}
                    dataMultipleFormImage.append(blank)
                    validFAllImage = False
                    formErrors.append(form) 
        
        if validFResource and validFAllImage:
            resource = formResource.save()
            if hasImage == True:
                for form in formMultipleImageTR:
                    imageResource = form.save(commit=False)
                    imageResource.idTouristResource = resource
                    imageResource.save()
            return HttpResponseRedirect(request.POST['urlBack'])
        else:
            
            MultipleFormSetTouristResourceImage = formset_factory(TouristResourceImageAddForm,
                                                     formset=util.RequeridFormSet,
                                                     can_delete=True)
            
            if len(dataMultipleFormImage) > 0:
                MultipleFormSetTouristResourceImage = formset_factory(TouristResourceImageAddForm,
                                                     extra=0,max_num=20)
            formMultipleImageTR = MultipleFormSetTouristResourceImage(initial = dataMultipleFormImage)
            
            self.data['form'] = formResource
            self.data['urlBack'] = request.POST['urlBack']
            self.data['formMultipleImageTR'] = formMultipleImageTR
            self.data['formErrors'] = formErrors
            return render(request,self.template_name,self.data)
            
    
class UpdateTouristResource(ViewApp):
    
    template_name = 'update_touristresource.html'
    form_class = TouristResourceUpdateForm
    
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateTouristResource, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, resource_id, *args, **kwargs):
        return super(UpdateTouristResource,self).get(request, *args, **kwargs)
    
    def post(self, request, resource_id, *args, **kwargs):
        return super(UpdateTouristResource,self).post(request, *args, **kwargs)
    

class DetailsTouristResource(ViewApp):
    
    template_name = 'details_touristresource.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super(DetailsTouristResource, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, resource_id, *args, **kwargs):
        
        host = request.META['HTTP_HOST']
        referer = request.META['HTTP_REFERER']
        url = referer.split(host)[1]
        
        try:
            resource = TouristResource.objects.get(id=resource_id)
            images = TouristResourceImage.objects.filter(idTouristResource=resource)
            self.data = self.getDataInit(request)
            self.data['resource'] = resource
            self.data['images'] = images
            util.generateQRTouristResource(request,resource) 
            return render(request,self.template_name,self.data)
        except TouristResource.DoesNotExist:
            return HttpResponseRedirect(url)
        
    def post(self, request, resource_id, *args, **kwargs):
        return self.get(request,resource_id,*args,**kwargs)
    

def removeTouristResource(request, resource_id, *arqs, **kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    try:
        resource = TouristResource.objects.get(id=resource_id)
        images = TouristResourceImage.objects.filter(idTouristResource=resource)
        for image in images:
            #TODO borrar del disco duro las imagenes 
            pass
        #TODO borrar la imagen QR del recurso en disco
        resource.delete()
    except TouristResource.DoesNotExist:
        pass
    finally:
        return HttpResponseRedirect(url)
    
    
    