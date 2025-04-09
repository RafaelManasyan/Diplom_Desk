from rest_framework import serializers

from addesk.models import Advert, Review


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
