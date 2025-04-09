from django.urls import path
from addesk.views import (
    AdvertListAPIView,
    AdvertCreateAPIView,
    AdvertRetrieveUpdateDestroyAPIView,
    ReviewListAPIView,
    ReviewCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView,
)


app_name = 'addesk'


urlpatterns = [
    path('adverts/', AdvertListAPIView.as_view(), name='advert-list'),
    path('advert/', AdvertCreateAPIView.as_view(), name='advert-create'),
    path('advert/<int:pk>/', AdvertRetrieveUpdateDestroyAPIView.as_view(), name='advert-detail'),

    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
]