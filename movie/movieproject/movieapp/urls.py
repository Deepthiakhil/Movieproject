from . import views
from django.urls import path
app_name='movieapp'
urlpatterns = [

    path('',views.allProCat,name='allProCat'),
    path('search/', views.SearchResult, name='SearchResult'),
    path('add/', views.add_movie, name='add_movie'),
    path('<slug:c_slug>/', views.allProCat, name='product_by_category'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<slug:c_slug>/<slug:movie_slug>/', views.proDetail, name='prodCatdetail'),




]