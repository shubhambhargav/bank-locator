"""Filters for banks"""
import django_filters as filters

from .models import BranchModel


class BranchFilter(filters.FilterSet):
    """Branch filter"""
    bank = filters.CharFilter(field_name='bank__name', lookup_expr='exact', required=True)
    city = filters.CharFilter(field_name='city', lookup_expr='exact', required=True)

    class Meta:
        model = BranchModel
        fields = ('bank', 'city')
