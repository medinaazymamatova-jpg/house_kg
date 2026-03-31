from .models import Property, Region, City, District
from modeltranslation.translator import TranslationOptions,register

@register(Property)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')




