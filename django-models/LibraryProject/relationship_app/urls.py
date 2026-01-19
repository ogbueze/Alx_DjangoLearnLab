from django.urls import path
from . import views
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books

urlpatterns = [
    path("", views.index, name="index"),
    path('books/', list_books, name="books"),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout'), name='logout'),
    path('register/', views.register, name='register'),
]