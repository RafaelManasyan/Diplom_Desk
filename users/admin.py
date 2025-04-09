from django.contrib import admin

from users.models import User


@admin.register(User)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['email', 'role', 'first_name', 'last_name']