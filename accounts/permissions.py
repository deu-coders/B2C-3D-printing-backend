from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return  True
    
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
    
        return obj.author == request.user