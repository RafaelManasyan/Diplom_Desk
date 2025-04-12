from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели пользователя."""

    class Meta:
        model = User
        fields = "__all__"


class PasswordResetSerializer(serializers.Serializer):
    """Сериализатор для запроса сброса пароля по email."""

    email = serializers.EmailField()

    def validate_email(self, value):
        """Проверяет, существует ли пользователь с указанным email."""
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email не найден.")
        return value


class SetNewPasswordSerializer(serializers.Serializer):
    """Сериализатор для установки нового пароля по токену сброса."""

    password = serializers.CharField(write_only=True, min_length=8)
    token = serializers.CharField(write_only=True)
    uid = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """Проверяет корректность UID и токена, валидирует нового пользователя."""
        try:
            uid = force_str(urlsafe_base64_decode(attrs["uid"]))
            user = User.objects.get(id=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError("Неверный UID.")

        if not PasswordResetTokenGenerator().check_token(user, attrs["token"]):
            raise serializers.ValidationError("Неверный или просроченный токен.")

        self.user = user
        return attrs
