from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'stories'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('contact-us/', views.contact_us, name= 'contact-us'),
    path('story/<int:pk>/', views.story, name= 'story'),
    path('older-children/', views.older_children, name='older-children'),
    path('young-children/', views.young_children, name='young-children'),
    path('search/', views.search_result, name='search-result'),
    path('master/', views.master, name='master'),
    path('category/<int:pk>/', views.category, name='category'),
]