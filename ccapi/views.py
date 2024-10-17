from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import EmployeeDetails, Employeecount, CustomerDetail, CustomerPurchase, VendorPurchase,vendorsales
from .serializers import (
    EmployeeDetailsSerializer, 
    EmployeecountSerializer, 
    CustomerDetailSerializer, 
    CustomerPurchaseSerializer, 
    VendorPurchaseSerializer,
    vendorsalesSerializer
)


class EmployeeDetailsListCreate(generics.ListCreateAPIView):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    parser_classes = (MultiPartParser, FormParser)

class EmployeeDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    parser_classes = (MultiPartParser, FormParser)


class EmployeecountListCreate(generics.ListCreateAPIView):
    queryset = Employeecount.objects.all()
    serializer_class = EmployeecountSerializer

class EmployeecountDetailRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employeecount.objects.all()
    serializer_class = EmployeecountSerializer


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

class VendorPurchaseListCreateView(generics.ListCreateAPIView):
    queryset = VendorPurchase.objects.all()
    serializer_class = VendorPurchaseSerializer

class VendorPurchaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorPurchase.objects.all()
    serializer_class = VendorPurchaseSerializer

class vendorsalesListCreateView(generics.ListCreateAPIView):
    queryset = vendorsales.objects.all()
    serializer_class = vendorsalesSerializer

class vendorsalesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = vendorsales.objects.all()
    serializer_class = vendorsalesSerializer    