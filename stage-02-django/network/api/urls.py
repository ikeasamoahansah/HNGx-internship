from django.urls import path
from .views import *

urlpatterns = [

    path('', api_root),
    
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetail.as_view(), name="user-detail"),
]