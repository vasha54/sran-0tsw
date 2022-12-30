from touristresource.models import TourismType, ValueTouristic, TypeService
from modeltranslation.translator import TranslationOptions,register

@register(TourismType)
class TourismTypeTranslationOptions(TranslationOptions):
    fields = ['type','description']
    
@register(ValueTouristic)
class ValueTouristicTranslationOptions(TranslationOptions):
    fields = ['value','description']
    
@register(TypeService)
class TypeServiceTranslationOptions(TranslationOptions):
    fields = ['type','description']
    
    
