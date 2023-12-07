from django.urls import path
from .views import BookingListAPIView 
from .views import MenuListAPIView
from . import views

urlpatterns = [
    path('bookings/', BookingListAPIView.as_view(), name='booking-list'),
    path ('menu/',MenuListAPIView.as_view(), name = 'menu-list'),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings', views.bookings, name='bookings')
    # Add more URL patterns as needed
]
