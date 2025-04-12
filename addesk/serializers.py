from rest_framework import serializers
from addesk.models import Advert, Review


class AdvertSerializer(serializers.ModelSerializer):
    """Сериализатор для модели объявлений.
    Используется для отображения и валидации данных объявлений.
    Поле 'author' исключено, так как устанавливается автоматически.
    """
    class Meta:
        model = Advert
        exclude = ["author"]


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели отзывов.
    Применяется для создания и отображения отзывов к объявлениям.
    Поле 'author' также исключено и задаётся автоматически.
    """
    class Meta:
        model = Review
        exclude = ["author"]
