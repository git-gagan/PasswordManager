from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='registerUser'),
    path('login/', views.loginUser, name='loginUser'),
    path('', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('insert/', views.insertData, name='insertData')
]