from django.urls import path

from . import views


app_name = 'store'

urlpatterns = [
    path('', views.BooksListView.as_view(), name='book_list'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
]