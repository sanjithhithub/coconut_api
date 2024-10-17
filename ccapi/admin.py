from django.contrib import admin
from .models import  EmployeeDetails,Employeecount,CustomerDetail,CustomerPurchase,VendorPurchase,vendorsales

admin.site.register(EmployeeDetails),
admin.site.register(Employeecount),
admin.site.register(CustomerDetail),
admin.site.register(CustomerPurchase),
admin.site.register(VendorPurchase),
admin.site.register(vendorsales)





# Register your models here.
