from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:book_id>/update/', views.update_book, name='update_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('books/', views.book_list, name='book_list'),
]
