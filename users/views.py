from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer, PasswordResetSerializer, SetNewPasswordSerializer


class RegistrationAPIView(CreateAPIView):
    """Регистрация нового пользователя с установкой пароля.

    Пользователь создаётся с активным статусом.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class ResetPasswordAPIView(generics.GenericAPIView):
    """Запрос на сброс пароля. Отправляет письмо с ссылкой на восстановление."""

    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_url = f"{settings.FRONTEND_URL}/users/reset_password_confirm/{uid}/{token}/"

            send_mail(
                'Восстановление пароля',
                f'Перейдите по ссылке для сброса пароля: {reset_url}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )

        return Response(
            {"detail": "Если пользователь с таким email существует, отправлена ссылка на сброс пароля."},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmAPIView(APIView):
    """Подтверждение сброса пароля. Устанавливает новый пароль пользователю."""

    def post(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        new_password = serializer.validated_data['password']

        user.set_password(new_password)
        user.save()

        return Response({"detail": "Пароль успешно изменён"}, status=status.HTTP_200_OK)