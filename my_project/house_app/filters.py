from django_filters.rest_framework import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'region' : ['exact'],
            'city' : ['exact'],
            'district': ['exact'],
            'type_transaction': ['exact'],
            'price' : ['lt', 'gt'],
            'area': ['lt', 'gt'],
            'room': ['exact'],
            'condition': ['exact'],
        }