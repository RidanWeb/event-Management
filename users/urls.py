from django.urls import path
from users.views import sign_out, sign_up, signin


urlpatterns = [
    
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', signin, name='sign_in'),
    path('sign_out/', sign_out, name='logout'),

    
    
]