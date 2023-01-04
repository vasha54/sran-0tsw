from touristresource.models import TourismType, ValueTouristic, TypeService, ScheduleService, ResourceTourist, TouristResourceImage
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
    
@register(ScheduleService)
class ScheduleServiceTranslationOptions(TranslationOptions):
    fields = ['name']
    
@register(ResourceTourist)
class ResourceTouristTranslationOptions(TranslationOptions):
    fields = ['name','description','history']
    
@register(TouristResourceImage)
class ResourTouristResourceImageTranslationOptions(TranslationOptions):
    fields = ['name','description']
    
    
