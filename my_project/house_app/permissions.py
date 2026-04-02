from rest_framework.permissions import BasePermission

class BuyerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'buyer'

class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'seller'