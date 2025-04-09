from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Просмотр доступен всем аутентифицированным,
    изменение/удаление — только автору или админу.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return obj.author == request.user or request.user.role == 'admin'
