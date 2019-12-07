"""Bank urls"""
from django.conf.urls import url
from django.urls import path

from .views import BranchDetailView, BranchListView

urlpatterns = [
    path('', BranchListView.as_view(), name='branch-list'),
    path('<str:pk>/', BranchDetailView.as_view(), name='branch-detail')
]
