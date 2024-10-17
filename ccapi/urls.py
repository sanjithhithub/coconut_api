from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import (
    CustomerDetailListCreateView, 
    CustomerDetailRetrieve,
    CustomerPurchaseListCreateView, 
    CustomerPurchaseRetrieveUpdateDestroyView,
    VendorPurchaseListCreateView,
    VendorPurchaseRetrieveUpdateDestroyView,
    EmployeecountListCreate,
    EmployeecountDetailRetrieve,
    vendorsalesListCreateView,
    vendorsalesRetrieveUpdateDestroyView
)

# Swagger Schema Configuration
schema_view = get_schema_view(
   openapi.Info(
      title="Coconut API Documentation",
      default_version='v1',
      description="This API handles customer purchases and employee management.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="msanjith130@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Employee API Endpoints
    path('employee-details/', views.EmployeeDetailsListCreate.as_view(), name='employee-details-list-create'),
    path('employee-details/<int:pk>/', views.EmployeeDetailsDetail.as_view(), name='employee-details-detail'),


    # Employee Count Endpoints
    path('employeecount/', EmployeecountListCreate.as_view(), name='employeecount-list-create'),
    path('employeecount/<int:pk>/', EmployeecountDetailRetrieve.as_view(), name='employeecount-detail'),

    # Customer API Endpoints
    path('customers/', CustomerDetailListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailRetrieve.as_view(), name='customer-detail'),

    # Purchase API Endpoints
    path('purchases/', CustomerPurchaseListCreateView.as_view(), name='purchase-list-create'),
    path('purchases/<int:pk>/', CustomerPurchaseRetrieveUpdateDestroyView.as_view(), name='purchase-detail'),

    # Vendor Purchase Endpoints
    path('vendorpurchase/', VendorPurchaseListCreateView.as_view(), name='vendor-list-create'),
    path('vendorpurchase/<int:pk>/', VendorPurchaseRetrieveUpdateDestroyView.as_view(), name='vendorpurchase-detail'),
    path('vendorsales/', vendorsalesListCreateView.as_view(),name = 'vendorsales-list-create'),
    path('vendorsales/<int:pk>/', vendorsalesRetrieveUpdateDestroyView.as_view(),name = 'vendorsales'),

    # Swagger Documentation Endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=1), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


