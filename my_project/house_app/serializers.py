from rest_framework import serializers
from .models import UserProfile, Region, City, District, Property, PropertyImage, Review


class UserProfileRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'password']

    def create(self, validated_data):
        return UserProfile.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'region_name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name', 'region']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'district_name', 'city']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'property_image']


class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True, source='propertyimage_set')

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'property_type', 'type_transaction',
            'region', 'city', 'district', 'address', 'area', 'price',
            'room', 'floor', 'total_floor', 'condition', 'document', 'seller', 'images'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'seller', 'buyer', 'rating', 'comment', 'created_at']