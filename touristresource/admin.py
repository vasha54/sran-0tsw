from django.contrib import admin
from touristresource.models import TourismType, TypeService, Schedule, InfrastructureAccess#, ResourceTourist, ScheduleService, Service, TouristResourceVideo, TouristResourceImage, ValueTouristic, ValueResourceTourist, TourismTypeResourceTourist
from touristresource.forms import TourismTypeForm, TypeServiceForm, ScheduleForm, InfrastructureAccessForm#, ValueTouristicForm, ScheduleServiceForm
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

admin.site.register(TourismType, TourismTypeAdmin)
admin.site.register(TypeService,TypeServiceAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(InfrastructureAccess,InfrastructureAccessAdmin)

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

            
    
    