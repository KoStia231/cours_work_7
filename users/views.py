from rest_framework import viewsets, status, generics
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.models import User

from users.serializers import (
    MyTokenObtainPairSerializer,
    MyTokenRefreshSerializer, UserSerializer
)


# ------------------------------------------------------ юзеры ------------------------------------------------------
class UserCreateView(generics.CreateAPIView):
    """Создание нового юзера"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
        return super().perform_create(serializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для просмотра, редактирования и деактивации пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Возвращает список пользователей в зависимости от прав доступа.
        """
        if self.request.user.has_perm('users.is_admin'):
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST', detail='Создание профиля через этот эндпоинт запрещено.')

    def destroy(self, request, *args, **kwargs):
        """
        Деактивирует пользователя вместо его удаления.
        """
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'status': 'Профиль удален'}, status=status.HTTP_204_NO_CONTENT)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
    permission_classes = [AllowAny]
