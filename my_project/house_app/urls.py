from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'cities', CityViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'images', PropertyImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('property/', PropertyListAPIView.as_view(), name='property_list'),
    path('property/<int:pk>', PropertyDetailAPIView.as_view(), name='property_detail'),
    path('review/', ReviewListAPIView.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetailAPIView.as_view(), name='review_detail'),
]