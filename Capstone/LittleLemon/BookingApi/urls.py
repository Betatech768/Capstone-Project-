from django.urls import path
from .views import BookingListAPIView 
from .views import MenuListAPIView

urlpatterns = [
    path('bookings/', BookingListAPIView.as_view(), name='booking-list'),
    path ('menu/',MenuListAPIView.as_view(), name = 'menu-list')
    # Add more URL patterns as needed
]
