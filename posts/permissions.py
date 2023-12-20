from rest_framework import permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    # Check if user has permissions to do something in object or not.
    def has_object_permission(self, request, view, obj):
    # Check if HTTP method of request is safe ways or not..
    # Safe ways => (GET, HEAD, OPTIONS) -Only Read-.
        if request.method in permissions.SAFE_METHODS:
            return True
    # If not safe ways;
    # check if user that send request is the same author of post or not.
        return obj.author == request.user

class IsAuthorOrReadOnlyUser(permissions.BasePermission):
    # Check if user has permissions to do something in object or not.
    def has_object_permission(self, request, view, obj):
    # Check if HTTP method of request is safe ways or not..
    # Safe ways => (GET, HEAD, OPTIONS) -Only Read-.
        if request.method in permissions.SAFE_METHODS:
            return True
    # If not safe ways;
    # check if user that send request is the same author of post or not.
        return obj.id == request.user.id