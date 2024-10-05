from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import EmployeeDetails, Employee
from .serializers import EmployeeDetailsSerializer, EmployeeSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .models import CustomerDetail
from .serializers import CustomerDetailSerializer
from .models import CustomerPurchase
from .serializers import CustomerPurchaseSerializer

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


class CustomerDetailListCreateView(generics.ListCreateAPIView):
    queryset = CustomerDetail.objects.all()
    serializer_class = CustomerDetailSerializer

class CustomerDetailRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerDetail.objects.all()
    serializer_class = CustomerDetailSerializer    



class CustomerPurchaseListCreateView(generics.ListCreateAPIView):
    queryset = CustomerPurchase.objects.all()
    serializer_class = CustomerPurchaseSerializer

class CustomerPurchaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerPurchase.objects.all()
    serializer_class = CustomerPurchaseSerializer
 
