import django.contrib.auth.views as auth_views
from django.urls import path
from . import views
from django.contrib import admin

app_name='notes'
urlpatterns =[
    path('', views.index,name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='notes/loggedout.html'),name='logout'),
    #path('login/', views.login,name='login'),
    path('home/', views.home_page,name='home_page'),
    path('register/', views.register,name='register'),
    path('settings/', views.settings,name='settings'),
    path('loggedout/', views.loggedout,name='loggedout'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/', views.delete,name='delete'),
]
