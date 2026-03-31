from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
import nested_admin

class DistrictInline(nested_admin.NestedTabularInline):
    model = District
    extra = 1

class CityInline(nested_admin.NestedStackedInline):
    model = City
    extra = 1
    inlines = [DistrictInline]

class RegionAdmin(nested_admin.NestedModelAdmin):
    model = Region
    inlines = [CityInline]


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(TranslationAdmin):
    inlines = [PropertyImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Region, RegionAdmin)
admin.site.register(Review)


