from touristresource.models import TourismType, TypeService, Schedule, InfrastructureAccess#, ValueTouristic, ScheduleService, ResourceTourist, TouristResourceImage
from modeltranslation.translator import TranslationOptions,register

@register(TourismType)
class TourismTypeTranslationOptions(TranslationOptions):
    fields = ['name','description']
    
@register(TypeService)
class TypeServiceTranslationOptions(TranslationOptions):
    fields = ['name','description']
    
@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ['name']
    
@register(InfrastructureAccess)
class InfrastructureAccessTranslationOptions(TranslationOptions):
    fields = ['name']
    
# @register(ValueTouristic)
# class ValueTouristicTranslationOptions(TranslationOptions):
#     fields = ['value','description']
    

    
# @register(ScheduleService)
# class ScheduleServiceTranslationOptions(TranslationOptions):
#     fields = ['name']
    
# @register(ResourceTourist)
# class ResourceTouristTranslationOptions(TranslationOptions):
#     fields = ['name','description','history']
    
# @register(TouristResourceImage)
# class ResourTouristResourceImageTranslationOptions(TranslationOptions):
#     fields = ['name','description']
    
    
