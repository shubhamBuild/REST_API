from django.urls import path
from .views import get_users, create_user ,user_detail

urlpatterns =[
    path ('Users/', get_users, name='get_users'),    
    path ('Users/create', create_user, name='create_user'),
    path ('Users/<int:pk>', user_detail, name='user_detail')
]