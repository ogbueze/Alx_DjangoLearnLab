from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path("", views.index, name="index"),
    path('books/',views.list_books, name="books"),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]