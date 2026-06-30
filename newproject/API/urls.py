from django.urls import path
from .views import get_user, create_user 

urlpatterns =[
    path ('Users/', get_user, name='get_user' ),    
    path ('Users/create', create_user, name='create_user' )
]