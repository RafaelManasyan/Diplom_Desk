from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

from addesk.filters import AdvertFilter
from addesk.models import Advert, Review
from addesk.permissions import IsAuthorOrReadOnly
from addesk.serializers import AdvertSerializer, ReviewSerializer


class AdvertListAPIView(ListAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertFilter


class AdvertCreateAPIView(CreateAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdvertRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = [IsAuthorOrReadOnly]


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrReadOnly]
