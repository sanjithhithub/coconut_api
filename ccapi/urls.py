from django.urls import path
from . import views
from .views import CustomerDetailListCreateView, CustomerDetailRetrieve
from .views import CustomerPurchaseListCreateView, CustomerPurchaseRetrieveUpdateDestroyView


from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
from .views import (
    CustomerDetailListCreateView, 
    CustomerDetailRetrieve,
    CustomerPurchaseListCreateView, 
    CustomerPurchaseRetrieveUpdateDestroyView
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
    # API Endpoints
    path('employee-details/', views.EmployeeDetailsListCreate.as_view(), name='employee-details-list-create'),
    path('employee-details/<int:pk>/', views.EmployeeDetailsDetail.as_view(), name='employee-details-detail'),
    path('employee/', views.EmployeeListCreate.as_view(), name='employee-list-create'),
    path('customers/', CustomerDetailListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailRetrieve.as_view(), name='customer-detail'),
    path('purchases/', CustomerPurchaseListCreateView.as_view(), name='purchase-list-create'),
    path('purchases/<int:pk>/', CustomerPurchaseRetrieveUpdateDestroyView.as_view(), name='purchase-detail'),

    # Swagger Documentation Endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


