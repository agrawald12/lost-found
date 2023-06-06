from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('signup/',views.signup, name='signup'),
    path('',views.user_login, name='signin'),
    path('index/',views.index,name="index"),
    path('logout/',views.user_logout,name='logout'),    

]
