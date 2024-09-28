from django.urls import path
from . import views
urlpatterns = [
    path('livro/', views.Livro),
    path('livro/<int:pk>/', views.livroById),
]