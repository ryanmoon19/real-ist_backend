from rest_framework.permissions import BasePermission, AllowAny

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        print("CustomPermission.has_permission called")
        # Allow any user to access the view
        return True