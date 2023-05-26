from modeltranslation.translator import TranslationOptions,register
from country.models import Province, Municipality

@register(Province)
class ProvinceTranslationOptions(TranslationOptions):
    fields = ['name']
    
@register(Municipality)
class MunicipalityTranslationOptions(TranslationOptions):
    fields = ['name']