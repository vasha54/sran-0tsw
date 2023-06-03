from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html

from touristresource.models import TourismType, TypeService, Schedule, InfrastructureAccess, ResourceTourist,MediaImageRT, TourismTypeResourceTourist,InfrastructureAccessResourceTourist,Service #, ResourceTourist, ScheduleService, Service, TouristResourceVideo, TouristResourceImage, ValueTouristic, ValueResourceTourist, TourismTypeResourceTourist
from touristresource.forms import TourismTypeForm, TypeServiceForm, ScheduleForm, InfrastructureAccessForm, ResourceTouristForm#, ValueTouristicForm, ScheduleServiceForm
from touristresource.views import ResourceTouristDetailsView,ResourceTouristQRsView,ResourceTouristQRPrintView,updateQRThisResourceTourist

from modeltranslation.admin import TranslationAdmin

from core import util
from core.settings import ITEM_PER_PAGE
# Register your models here.

class TourismTypeAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['name','descriptionShort']
    search_fields = ['name__contains','description__contains']
    
    form = TourismTypeForm
    model = TourismType
    group_fieldsets = True
    
    class Media:
        pass
    
    @admin.display(ordering='description')    
    def descriptionShort(self,_obj):
        return _obj.descriptionShort()
    descriptionShort.short_description = "Descripción"
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.name)
            super().save_model(request, obj, self.form, change)
            
class TypeServiceAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['name','descriptionShort']
    search_fields = ['name__contains','description__contains']
    
    form = TypeServiceForm
    model = TypeService
    group_fieldsets = True
    
    class Media:
        pass
    
    @admin.display(ordering='description')    
    def descriptionShort(self,_obj):
        return _obj.descriptionShort()
    descriptionShort.short_description = "Descripción"
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.name)
            super().save_model(request, obj, self.form, change)
            
class ScheduleAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['name','startTime', 'endTime']
    search_fields = ['name__contains','startTime__hour','startTime__minute','endTime__hour','endTime__minute']
    
    form = ScheduleForm
    model = Schedule
    group_fieldsets = True
    
    fieldsets = (
            ("Nombre",{"fields": ("name",)},),
            ("Horario",{"fields": ('startTime','endTime',)},),
            
        )
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.name)
            super().save_model(request, obj, self.form, change)

class InfrastructureAccessAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['name']
    search_fields = ['name__contains']
    
    form = InfrastructureAccessForm
    model = InfrastructureAccess
    group_fieldsets = True
    
    class Media:
        pass
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.name)
            super().save_model(request, obj, self.form, change)

class ResourceTouristImageInline(admin.TabularInline):
    model = MediaImageRT
    extra = 1
    verbose_name_plural = 'Imágenes'
    
class ResourceTouristTourismTypeInline(admin.TabularInline):
    model = TourismTypeResourceTourist
    extra = 1
    verbose_name_plural = 'Tipos de turismo'
    
    
class ResourceTouristInfrastructureAccessInline(admin.TabularInline):
    model = InfrastructureAccessResourceTourist
    extra = 1
    verbose_name_plural = 'Infraestructuras vial de acceso'

class ResourceTouristServiceInline(admin.TabularInline):
    model = Service
    extra = 1
    verbose_name_plural = 'Servicios'

class ResourceTouristAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['name','idMunicipality','geoLocLat','geoLocLon','service','links']
    search_fields = ['name__contains','description__contains','comments__contains','address__contains','idMunicipality__name']
    
    inlines = [ResourceTouristTourismTypeInline,ResourceTouristInfrastructureAccessInline,ResourceTouristServiceInline,ResourceTouristImageInline]
    
    form = ResourceTouristForm
    model = ResourceTourist
    group_fieldsets = True
    
    fieldsets = (
            ("Nombre",{"fields": ("name",)},),
            ("General",{"fields": ('idMunicipality','location',)},),
            ("Dirección",{"fields": ("address",)},),
            ("Descripción",{"fields": ("description",)},),
            ("Otros comentarios",{"fields": ("comments",)},),
        )
    
    def links(self,_obj):
        urlViewDetails = reverse("admin:resource_tourist_view_details", args=[_obj.pk])
        urlView = '/resource_tourist/'+str(_obj.pk)
        urlViewApk = '/api/v1/resource_tourist/'+str(_obj.pk)
        urlPrintQR = reverse("admin:resource_tourist_print_qr", args=[_obj.pk])
        urlUpdateQR = reverse("admin:resource_tourist_update_qr", args=[_obj.pk])
        urlViewQR = reverse("admin:resource_tourist_view_qr", args=[_obj.pk])
        urlStadistics = reverse("admin:resource_tourist_view_qr", args=[_obj.pk])
        
        linkHtmlDetails = format_html(f'<a href="{urlViewDetails}" class="linkListAdmin" ><i class="fas fa-eye" title="Detalles"></i></a>')
        linkHtmlStadistics= format_html(f'<a href="{urlStadistics}" class="linkListAdmin" ><i class="fas fa-chart-bar" title="Estadísticas"></i></a>')
        linkHtmlViewQR = format_html(f'<a href="{urlViewQR}" class="linkListAdmin" ><i class="fas fa-qrcode" title="QR del recurso"></i></a>')
        linkHtmlPrintQR = format_html(f'<a target="blank" href="{urlPrintQR}" class="linkListAdmin" ><i class="fas fa-print" title="Imprimir QR"></i></a>')
        linkHtmlUpdateQR = format_html(f'<a href="{urlUpdateQR}" class="linkListAdmin" ><i class="fas fa-undo" title="Actualizar QR"></i></a>')
        linkHtmlView = format_html(f'<a target="blank" href="{urlView}" class="linkListAdmin" ><i class="fas fa-tablet-alt" title="Ver recurso en la web"></i></a>')
        linkHtmlViewApk = format_html(f'<a target="blank" href="{urlViewApk}" class="linkListAdmin" ><i class="fas fa-exchange-alt" title="Ver recurso en API"></i></a>')
        linkHtmlRemove = format_html(f'<a href="/admin/touristresource/resourcetourist/{_obj.pk}/delete/" class="linkListAdmin"><i class="fas fa-trash-alt" title="Eliminar"></i></a>')
        
        
        return linkHtmlDetails+linkHtmlStadistics+linkHtmlView+linkHtmlViewApk+linkHtmlUpdateQR+linkHtmlViewQR+linkHtmlPrintQR+linkHtmlRemove
    links.short_description=''
    
    def service(self,_obj):
        return ''
    service.short_description='Servicios'
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            location = form.cleaned_data['location']
            location = location.split(',')
            obj.geoLocLat = float(location[0])
            obj.geoLocLon = float(location[1])
            obj.slug = util.generateSLUG(obj.name)
            super().save_model(request, obj, self.form, change)
    
    def get_urls(self):
        return [
             path("view/<pk>",ResourceTouristDetailsView.as_view(),name=f"resource_tourist_view",),
             path("apk/<pk>",ResourceTouristDetailsView.as_view(),name=f"resource_tourist_view_apk",),
             
             path("stadistics/<pk>",self.admin_site.admin_view(ResourceTouristDetailsView.as_view()),name=f"resource_tourist_view_stadistics",),
             path("view_details/<pk>",self.admin_site.admin_view(ResourceTouristDetailsView.as_view()),name=f"resource_tourist_view_details",),
             path("update_qr/<pk>",self.admin_site.admin_view(updateQRThisResourceTourist),name=f"resource_tourist_update_qr",),
             path("print_qr/<pk>",self.admin_site.admin_view(ResourceTouristQRPrintView.as_view()),name=f"resource_tourist_print_qr",),
             path("view_qr/<pk>",self.admin_site.admin_view(ResourceTouristQRsView.as_view()),name=f"resource_tourist_view_qr",),
            *super().get_urls(),
        ]

admin.site.register(MediaImageRT)
admin.site.register(TourismTypeResourceTourist)
admin.site.register(InfrastructureAccessResourceTourist)
admin.site.register(Service)
admin.site.register(TourismType, TourismTypeAdmin)
admin.site.register(TypeService,TypeServiceAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(InfrastructureAccess,InfrastructureAccessAdmin)
admin.site.register(ResourceTourist,ResourceTouristAdmin)

# class ResourceTouristAdmin(TranslationAdmin):
#     pass





# class ServiceAdmin(admin.ModelAdmin):
#     pass


# class TouristResourceVideoAdmin(admin.ModelAdmin):
#     pass


# class TouristResourceImageAdmin(TranslationAdmin):
#     pass


# class ValueTouristicAdmin(TranslationAdmin):
#     list_display=['value','descriptionShort']
#     search_fields = ['value__contains','description__contains']
    
#     form = ValueTouristicForm
#     model = ValueTouristic
#     group_fieldsets = True
    
#     class Media:
#         pass
    
#     @admin.display(ordering='description')    
#     def descriptionShort(self,_obj):
#         return _obj.descriptionShort()
#     descriptionShort.short_description = "Descripcion"
    
#     def save_model(self, request, obj, form, change):
        
#         if form.is_valid()==True:
#             obj = form.save(commit=False)
#             obj.slug = util.generateSLUG(obj.type)
#             super().save_model(request, obj, self.form, change)



            

# class ValueResourceTouristAdmin(admin.ModelAdmin):
#     pass


# class TourismTypeResourceTouristAdmin(admin.ModelAdmin):
#     pass



# 
# admin.site.register(ResourceTourist,ResourceTouristAdmin)
# 
# admin.site.register(Service,ServiceAdmin)
# admin.site.register(TouristResourceVideo,TouristResourceVideoAdmin)
# admin.site.register(TouristResourceImage,TouristResourceImageAdmin)
# admin.site.register(ValueTouristic,ValueTouristicAdmin)
# admin.site.register(TypeService,TypeServiceAdmin)
# admin.site.register(ValueResourceTourist,ValueResourceTouristAdmin)
# admin.site.register(TourismTypeResourceTourist,TourismTypeResourceTouristAdmin)

            
    
    