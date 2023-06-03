from django.urls import path
from .views import AdminUserView, UserCreateView


urlpatterns = [
  path('admin-users/', AdminUserView.as_view(), name='admin-users'),
  path('users/create/', UserCreateView.as_view(), name='user-create'),
]
