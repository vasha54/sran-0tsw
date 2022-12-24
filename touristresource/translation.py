from touristresource.models import TourismType
from modeltranslation.translator import TranslationOptions,register

@register(TourismType)

class TourismTypeTranslationOptions(TranslationOptions):
    fields = ('type','description')