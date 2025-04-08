from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.views import (PasswordResetConfirmAPIView, RegistrationAPIView,
                         ResetPasswordAPIView)

app_name = 'users'


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', RegistrationAPIView.as_view(), name='registration'),
    path('reset_password/', ResetPasswordAPIView.as_view(), name='reset_password'),
    path('reset_password_confirm/', PasswordResetConfirmAPIView.as_view(), name='reset_password_confirm'),
]
