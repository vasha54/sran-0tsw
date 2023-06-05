from touristresource.models import TouristAttraction, TourismType, TypeService, Schedule, InfrastructureAccess, ResourceTourist#, ValueTouristic, ScheduleService, ResourceTourist, TouristResourceImage
from modeltranslation.translator import TranslationOptions,register

@register(TouristAttraction)
class TouristAttractionTranslationOptions(TranslationOptions):
    fields = ['name','description']

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
    
@register(ResourceTourist)
class ResourceTouristTranslationOptions(TranslationOptions):
     fields = ['name','description','comments','address']
    

    
    
