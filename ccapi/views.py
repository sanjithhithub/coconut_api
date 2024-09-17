from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import EmployeeDetails, Employee
from .serializers import EmployeeDetailsSerializer, EmployeeSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class EmployeeDetailsListCreate(generics.ListCreateAPIView):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    parser_classes = (MultiPartParser, FormParser)

class EmployeeDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    parser_classes = (MultiPartParser, FormParser)

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
