from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Customer.objects.filter(email=email).exists():
            return Response({'error': 'A customer with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'Integrity error, duplicate email found.'}, status=status.HTTP_400_BAD_REQUEST)