from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.author_table),
    path('add_books', views.add_book),
    path('add_authors', views.add_author),
    path('books/<int:book_id>', views.show_book),
    path('authors/<int:author_id>', views.show_author),
    path('add_book_to_author/<int:author_id>', views.book_to_author),
    path('add_author_to_book/<int:book_id>', views.author_to_book)
]