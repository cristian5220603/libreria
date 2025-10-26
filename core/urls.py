from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('libro/<int:pk>/', views.book_detail, name='book_detail'),
    path('rentar/<int:pk>/', views.rentar_libro, name='rentar_libro'),
    path('mis-prestamos/', views.mis_prestamos, name='mis_prestamos'),
]
