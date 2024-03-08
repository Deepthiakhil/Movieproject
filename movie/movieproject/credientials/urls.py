from . import views
from django.urls import path

app_name = 'credientials'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('update/<int:id>/', views.update, name='update'),
]
