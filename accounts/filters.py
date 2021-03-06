import django_filters
from django_filters import DateFilter,CharFilter
from .models import *

class  OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="created_date", lookup_expr='gte')
    end_date = DateFilter(field_name="created_date", lookup_expr='lte')
    comment = CharFilter(field_name='comment', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'created_date']
