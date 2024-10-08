from django.utils import timezone
from decimal import Decimal, InvalidOperation
from django.db import models
from django.utils import timezone



class Employee(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining auto-increment field
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EmployeeDetails(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)
    photos = models.ImageField(upload_to='uploads/', null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    coconut_count = models.DecimalField(max_digits=10, decimal_places=1)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Ensure that `rate` is a valid decimal
        try:
            self.rate = Decimal(self.rate)
        except InvalidOperation:
            raise ValueError("Rate must be a valid decimal number.")

        
        if self.coconut_count and self.rate:
            self.amount = Decimal(self.coconut_count) * self.rate
        else:
            self.amount = Decimal('0.00')

       
        if isinstance(self.date, timezone.datetime):
            self.date = self.date.date()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.employee.name}"



class CustomerDetail(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    photo_upload = models.ImageField(upload_to='customer_photos/', blank=True, null=True)
 

    def __str__(self):
        return self.name
    

class CustomerPurchase(models.Model):
    coconut_count = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    date = models.DateTimeField(default=timezone.now) 
   

    def save(self, *args, **kwargs):
        if self.coconut_count is not None and self.rate is not None:
            self.amount = self.coconut_count * self.rate
        else:
            self.amount = 0
        super(CustomerPurchase, self).save(*args, **kwargs)


'''class vendorpurchase(models.model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)
    company = models.CharField(max_length=255)
    address = models.TextField()
    photo_upload = models.ImageField(upload_to='customer_photos/', blank=True, null=True)'''

    

  

    
   


