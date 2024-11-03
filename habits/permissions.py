from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Проверяет, является ли пользователь автором объекта.
    """
    def has_object_permission(self, request, view, obj):
        return obj.autor == request.user


# костыль
class IsUser(BasePermission):
    """
    Позволяет доступ к объекту только его владельцу.
    """

    def has_object_permission(self, request, view, obj):

        return request.user and request.user == obj
