from django.urls import path
from .views import AdminUserView


urlpatterns = [
  path('admin-users/', AdminUserView.as_view(), name='admin-users'),
]
