from django.contrib import admin

from addesk.models import Advert, Review


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'author', 'created_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'advert', 'created_at']
