from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect,  JsonResponse, HttpResponse
from django.forms import formset_factory
from django.shortcuts import render
from django.contrib import admin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import View

from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
import os
from datetime import datetime
import folium

from touristresource.models import MediaImageRT,ResourceTourist,InfrastructureAccessResourceTourist,TourismTypeResourceTourist,TouristAttractionResourceTourist, Service

from country.models import Language

from core.util import generateQRTouristResource
from core import settings


def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path 

class ResourceTouristDetailsView(PermissionRequiredMixin,View):
    permission_required = "touristresource.view_resourcetourist"
    template_name = 'resource_tourist_details.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        return {
            **admin.site.each_context(self.request),
        }
    
    def get(self,request, pk,*args, **kwargs):
        data = self.get_context_data(**kwargs)
        return render(request,self.template_name,data)
    
    def post(self,request, pk,*args, **kwargs):
        data = self.get_context_data(**kwargs)
        return render(request,self.template_name,data)
    

class ResourceTouristQRsView(PermissionRequiredMixin,View):
    permission_required = "touristresource.view_resourcetourist"
    template_name = 'resource_tourist_qrs.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        return {
            **admin.site.each_context(self.request),
        }
    
    def get(self,request, pk,*args, **kwargs):
        data = self.get_context_data(**kwargs)
        domainWeb = request.META['HTTP_HOST']
        protocol = 'http://'
        try:
            resource = ResourceTourist.objects.get(pk=pk)
            data['urlQRWeb'] = protocol + domainWeb+'/medias/qr_resources/web_'+str(resource.pk)+'.png'
            data['urlQRApp'] = protocol + domainWeb+'/medias/qr_resources/app_'+str(resource.pk)+'.png'
            data['resource'] = resource
        except ResourceTourist.DoesNotExist:
            pass
        return render(request,self.template_name,data)
    
    def post(self,request, pk,*args, **kwargs):
        self.get(request, pk,*args,**kwargs)

class ResourceTouristQRPrintView(PermissionRequiredMixin,View):
    permission_required = "touristresource.view_resourcetourist"
    template_name = 'resource_tourist_qrs_print.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        return {
            **admin.site.each_context(self.request),
        }
    
    def get(self,request, pk,*args, **kwargs):
        data = self.get_context_data(**kwargs)
        domainWeb = request.META['HTTP_HOST']
        protocol = 'http://'
        try:
            context_dict = {}
            resource = ResourceTourist.objects.get(pk=pk)
            context_dict['urlQRWeb'] = '/medias/qr_resources/web_'+str(resource.pk)+'.png'
            context_dict['urlQRApp'] = '/medias/qr_resources/app_'+str(resource.pk)+'.png'
            context_dict['resource'] = resource
            template = get_template(self.template_name)
            html  = template.render(context_dict)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), dest=result,link_callback=fetch_resources)
            if not pdf.err:
                return HttpResponse(result.getvalue(), content_type='application/pdf')
        except ResourceTourist.DoesNotExist:
            pass
        return HttpResponseRedirect(url)
    
    def post(self,request, pk,*args, **kwargs):
        self.get(request, pk,*args,**kwargs)
    
class ResourceTouristView(View):
    template_name = 'resource_tourist.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, pk,*args, **kwargs):
        languages = Language.objects.all().order_by('name_es')
        data ={'languages':languages}
        try :
            resource = ResourceTourist.objects.get(pk=pk)
            attractions = TouristAttractionResourceTourist.objects.filter(idResourceTourist=pk)
            type_tourism = TourismTypeResourceTourist.objects.filter(idResourceTourist=pk)
            infraestructures = InfrastructureAccessResourceTourist.objects.filter(idResourceTourist=pk)
            images = MediaImageRT.objects.filter(idResourceTourist=pk)
            ser = Service.objects.filter(idResourceTourist=pk)
            services= []
            
            status = ['text-muted','text-danger','text-warning']
            dateNow = datetime.now()
            
            for s in ser:
                s.setStatus(dateNow,status)
                services.append(s)
            
            services.sort()
            #Create Map Object 
            map = folium.Map(location=[resource.geoLocLat,resource.geoLocLon],zoom_start=18,zoom_control=False,no_touch=True)
            folium.Marker(location=[resource.geoLocLat,resource.geoLocLon]).add_to(map)
            #Get Html Represention
            map = map._repr_html_()
            
            data['resource'] = resource
            data['attractions'] = attractions
            data['infraestructures'] = infraestructures
            data['typetourism'] = type_tourism
            data['images'] = images
            data['latLocation'] = resource.geoLocLat
            data['lonLocation'] = resource.geoLocLon 
            data['services'] = services
            data['map'] = map
        except ResourceTourist.DoesNotExist:
            pass
        return render(request,self.template_name,data)
    
    def post(self,request, pk,*args, **kwargs):
        languages = Language.objects.all().order_by('pk')
        data ={'languages':languages}
        return render(request,self.template_name,data)

def updateQRThisResourceTourist(request,pk,*arg,**kwargs):
    host = request.META['HTTP_HOST']
    referer = request.META['HTTP_REFERER']
    url = referer.split(host)[1]
    
    try:
        resource = ResourceTourist.objects.get(pk=pk)
        generateQRTouristResource(request, resource)
        generateQRTouristResource(request, resource,False)
    except ResourceTourist.DoesNotExist:
        pass
    
    
    
    return HttpResponseRedirect(url)