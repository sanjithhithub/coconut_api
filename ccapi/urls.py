from django.urls import path
from . import views

urlpatterns = [
    path('employee-details/', views.EmployeeDetailsListCreate.as_view(), name='employee-details-list-create'),
    path('employee-details/<int:pk>/', views.EmployeeDetailsDetail.as_view(), name='employee-details-detail'),
    path('employee/', views.EmployeeListCreate.as_view(), name='employee-list-create'),
]
