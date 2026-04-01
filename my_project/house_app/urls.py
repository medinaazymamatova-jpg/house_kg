from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ( UserProfileViewSet,
                    RegionViewSet, CityViewSet, DistrictViewSet,
                    PropertyViewSet, PropertyImageViewSet, ReviewViewSet)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'cities', CityViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'images', PropertyImageViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]