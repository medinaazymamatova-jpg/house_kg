from rest_framework import serializers
from .models import UserProfile, Region, City, District, Property, PropertyImage, Review
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'role']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_name']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['property_image']


class PropertyListSerializer(serializers.ModelSerializer):
    property_images = PropertyImageSerializer(read_only=True, many=True)
    class Meta:
        model = Property
        fields = ['id', 'title',  'property_type', 'area', 'room', 'price', 'region',
                  'city', 'district', 'address', 'property_images']

class PropertyDetailSerializer(serializers.ModelSerializer):
    property_images = PropertyImageSerializer(read_only=True, many=True)
    city = CitySerializer()
    region = RegionSerializer()
    district = DistrictSerializer()
    seller = UserProfileNameSerializer()
    avg_rating = serializers.SerializerMethodField()
    count_review = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = ['title',  'property_type', 'area', 'room', 'price', 'region', 'type_transaction',
                  'city', 'description', 'district', 'address', 'property_images', 'condition', 'document', 'room',
                  'floor', 'total_floor','avg_rating', 'count_review', 'seller']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_review(self, obj):
        return obj.get_count_review()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    property = PropertyListSerializer()
    seller = UserProfileNameSerializer()
    created_at = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Review
        fields = ['id',  'seller', 'property', 'rating', 'comment', 'created_at']



class ReviewDetailSerializer(serializers.ModelSerializer):
    property = PropertyListSerializer()
    seller = UserProfileNameSerializer()
    created_at = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = Review
        fields = ['seller', 'property', 'rating', 'comment', 'created_at']