from django.contrib import admin
from django.urls import path, include
from bookstore import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('search',views.search, name='search' ),
    path('del_book/<int:pk>',views.del_book, name='del_book' ),
]