from django.contrib import admin

from addesk.models import Advert, Review


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Админка для модели объявлений."""
    list_display = ['title', 'price', 'author', 'created_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Админка для модели отзывов."""
    list_display = ['author', 'advert', 'created_at']
