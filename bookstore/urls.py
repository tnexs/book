from django.contrib import admin
from django.urls import path, include
from bookstore import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('search',views.search, name='search' ),
    path('delele/<int:id>',views.delete, name='delete' ),
]