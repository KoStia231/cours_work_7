from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from users.models import User


#  ------------------------------------------------------ юзеры ------------------------------------------------------

class RegisterUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'phone_number', 'telegram_chat_id']

    def validate(self, attrs):
        """Проверка на изменения системных полей"""
        read_only_fields = ['id', 'last_login', 'is_superuser', 'is_staff', 'groups', 'user_permissions']

        for field in read_only_fields:
            if field in attrs:
                raise serializers.ValidationError(f"Изменение поля '{field}' запрещено.")
        return attrs


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['first_name'] = user.first_name
        token['email'] = user.email

        return token


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    pass
