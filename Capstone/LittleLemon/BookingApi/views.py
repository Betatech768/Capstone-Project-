from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer
from .models import Menu
from .serializers import MenuSerializer
from django.shortcuts import render
from django.core import serializers
from datetime import datetime
import json
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item})

class BookingListAPIView(APIView):
    def get(self, request, format=None):
        # Retrieve all bookings from the database
        bookings = Booking.objects.all()

        # Serialize the bookings
        serializer = BookingSerializer(bookings, many=True)

        # Return the serialized data as a response
        return Response(serializer.data)

    def post(self, request, format=None):
        # Deserialize the incoming data
        serializer = BookingSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # Save the validated data to the database
            serializer.save()

            # Return a success response
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return an error response if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuListAPIView(APIView):
    def get(self, request, format=None):
        # Retrieve all menu items from the database
        menu_items = Menu.objects.all()

        # Serialize the menu items
        serializer = MenuSerializer(menu_items, many=True)

        # Return the serialized data as a response
        return Response(serializer.data)

    def post(self, request, format=None):
        # Deserialize the incoming data
        serializer = MenuSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # Save the validated data to the database
            serializer.save()

            # Return a success response
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return an error response if validation fails
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
