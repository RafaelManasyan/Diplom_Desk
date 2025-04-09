from rest_framework import serializers

from addesk.models import Advert, Review


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        exclude = ["author"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ["author"]
