from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only the author of a post or an admin user to edit or delete it.
    """
    def has_permission(self, request, view):
        # Allow all users to view posts (GET requests)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow only authenticated users to create posts (POST requests)
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        
        return True

    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Only allow the author or an admin to edit or delete
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user or request.user.is_staff
        
        return False
