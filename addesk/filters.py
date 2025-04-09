import django_filters
from addesk.models import Advert


class AdvertFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Advert
        fields = ['title']