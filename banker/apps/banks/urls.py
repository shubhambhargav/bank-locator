"""Bank urls"""
from django.conf.urls import url
from django.urls import path

from .views import BranchDetailView, BranchListView

urlpatterns = [
    path('branches/<str:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('branches/', BranchListView.as_view(), name='branch-list')
]
