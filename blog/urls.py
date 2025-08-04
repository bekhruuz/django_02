from django.urls import path
from .views import index_fronti, login_list

urlpatterns = [
    path('', index_fronti, name='lalala'),
    path('login/', login_list, name='login'),
]

