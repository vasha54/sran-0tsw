from django.contrib import admin
from touristresource.models import TourismType
from touristresource.forms import TourismTypeForm
from modeltranslation.admin import TranslationAdmin
from core import util
# Register your models here.


class TourismTypeAdmin(TranslationAdmin):
    list_display=['type','descriptionShort']
    
    form = TourismTypeForm
    model = TourismType
    group_fieldsets = True
    
    class Media:
        pass
    
    def descriptionShort(self,_obj):
        return _obj.descriptionShort()
    descriptionShort.short_description = "Descripcion"
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.type)
            super().save_model(request, obj, self.form, change)
            
admin.site.register(TourismType, TourismTypeAdmin)

            
    
    