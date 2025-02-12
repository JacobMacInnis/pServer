from django.urls import path
from .views import get_users, user_detail, create_user

urlpatterns = [
    path('users/', get_users, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail')
]