"""Bank views"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.pagination import LimitOffsetPagination

from .models import BranchModel
from .filters import BranchFilter
from .serializers import BranchSerializer, BranchSlimSerializer


class BranchDetailView(generics.RetrieveAPIView):
    """Object specific view for bank given the branch"""
    queryset = BranchModel.objects.all()
    serializer_class = BranchSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BranchListView(generics.ListAPIView):
    """Branch listing given city and bank name"""
    queryset = BranchModel.objects.all()
    serializer_class = BranchSlimSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = BranchFilter
    pagination_class = LimitOffsetPagination
