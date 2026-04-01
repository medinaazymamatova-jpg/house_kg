from rest_framework import serializers
from .models import UserProfile, Region, City, District, Property, PropertyImage, Review


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = 'all'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = 'all'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = 'all'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = 'all'


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = 'all'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = 'all'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'all'