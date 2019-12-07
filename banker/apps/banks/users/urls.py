"""Bank urls"""
from django.urls import path

from .views import CreateUserView, LoginView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/register/', CreateUserView.as_view(), name='auth-register')
]
