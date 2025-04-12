from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для модели пользователя."""
    list_display = ['email', 'role', 'first_name', 'last_name']
