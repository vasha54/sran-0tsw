from django.contrib import admin
from touristresource.models import TourismType, ResourceTourist, ScheduleService, Service, TouristResourceVideo, TouristResourceImage, ValueTouristic, TypeService
from touristresource.forms import TourismTypeForm, ValueTouristicForm, TypeServiceForm
from modeltranslation.admin import TranslationAdmin
from core import util
# Register your models here.


class TourismTypeAdmin(TranslationAdmin):
    list_display=['type','descriptionShort']
    search_fields = ['type__contains','description__contains']
    
    form = TourismTypeForm
    model = TourismType
    group_fieldsets = True
    
    class Media:
        pass
    
    @admin.display(ordering='description')    
    def descriptionShort(self,_obj):
        return _obj.descriptionShort()
    descriptionShort.short_description = "Descripcion"
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.type)
            super().save_model(request, obj, self.form, change)
 
class ResourceTouristAdmin(admin.ModelAdmin):
    pass


class ScheduleServiceAdmin(admin.ModelAdmin):
    pass


class ServiceAdmin(admin.ModelAdmin):
    pass


class TouristResourceVideoAdmin(admin.ModelAdmin):
    pass


class TouristResourceImageAdmin(admin.ModelAdmin):
    pass


class ValueTouristicAdmin(TranslationAdmin):
    list_display=['value','descriptionShort']
    search_fields = ['value__contains','description__contains']
    
    form = ValueTouristicForm
    model = ValueTouristic
    group_fieldsets = True
    
    class Media:
        pass
    
    @admin.display(ordering='description')    
    def descriptionShort(self,_obj):
        return _obj.descriptionShort()
    descriptionShort.short_description = "Descripcion"
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.type)
            super().save_model(request, obj, self.form, change)



class TypeServiceAdmin(TranslationAdmin):
    list_display=['type','descriptionShort']
    search_fields = ['type__contains','description__contains']
    
    form = TypeServiceForm
    model = TypeService
    group_fieldsets = True
    
    class Media:
        pass
    
    @admin.display(ordering='description')    
    def descriptionShort(self,_obj):
        return _obj.descriptionShort()
    descriptionShort.short_description = "Descripcion"
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.type)
            super().save_model(request, obj, self.form, change)
   
admin.site.register(TourismType, TourismTypeAdmin)
admin.site.register(ResourceTourist,ResourceTouristAdmin)
admin.site.register(ScheduleService,ScheduleServiceAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(TouristResourceVideo,TouristResourceVideoAdmin)
admin.site.register(TouristResourceImage,TouristResourceImageAdmin)
admin.site.register(ValueTouristic,ValueTouristicAdmin)
admin.site.register(TypeService,TypeServiceAdmin)

            
    
    