from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer

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
