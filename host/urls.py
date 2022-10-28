from django.urls import path
from .views import *
from django.contrib.auth import views as auth

from rest_framework.authtoken import views
urlpatterns=[
    path('',index,name='index'),
    path('login/', Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/',register, name='register'),

    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),

]