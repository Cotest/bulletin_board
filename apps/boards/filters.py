import django_filters

from .models import BoardPost


class BoardPostFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BoardPost
        fields = ['tags', 'category', 'text']