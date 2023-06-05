from django.contrib import admin
from django.utils.html import format_html

from modeltranslation.admin import TranslationAdmin
from core import util
from core.settings import ITEM_PER_PAGE

from country.models import Province,Municipality,Language
from country.forms import ProvinceForm, MunicipalityForm,LanguageForm
# Register your models here.

class PronviceAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['name','countMunicipality']
    search_fields = ['name__contains']
    
    form = ProvinceForm
    model = Province
    group_fieldsets = True
    
    class Media:
        pass
    
    @admin.display(ordering='countMunicipality')    
    def countMunicipality(self,_obj):
        return _obj.countMunicipality()
    countMunicipality.short_description = "Cantidad de municipios"
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.name)
            super().save_model(request, obj, self.form, change)
            
class MunicipalityAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['name','idProvince']
    search_fields = ['name__contains','idProvince__name']
    
    form = MunicipalityForm
    model = Municipality
    group_fieldsets = True
    
    class Media:
        pass
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.idProvince.slug+'_'+obj.name)
            super().save_model(request, obj, self.form, change)
            
class LanguageAdmin(TranslationAdmin):
    list_per_page = ITEM_PER_PAGE
    list_display=['flags','ISO639v1']
    search_fields = ['name__contains']
    
    form = LanguageForm
    model = Language
    group_fieldsets = True
    
    def flags(self,_obj):
        if _obj.flag !=None :
            return format_html('<img src="{}" width="24px" height="24px">  {}',_obj.flag.url,_obj.name)
    flags.short_description = "Nombre"
    
    class Media:
        pass
    
    def save_model(self, request, obj, form, change):
        
        if form.is_valid()==True:
            obj = form.save(commit=False)
            obj.slug = util.generateSLUG(obj.name)
            super().save_model(request, obj, self.form, change)
            
admin.site.register(Province, PronviceAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Language, LanguageAdmin)