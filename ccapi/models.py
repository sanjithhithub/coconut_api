from django.utils import timezone
from decimal import Decimal, InvalidOperation
from django.db import models
from django.utils import timezone




from django.utils import timezone

class EmployeeDetails(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)  # Editable ID field
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)
    photos = models.ImageField(upload_to='uploads/', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if isinstance(self.date, timezone.datetime):
            self.date = self.date.date()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

       

class Employeecount(models.Model):
    id = models.AutoField(primary_key=True,editable=True)  # Auto-incrementing id field
    coconut_count = models.DecimalField(max_digits=10, decimal_places=1)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            self.rate = Decimal(self.rate)
        except InvalidOperation:
            raise ValueError("Rate must be a valid decimal number.")

        if self.coconut_count and self.rate:
            self.amount = Decimal(self.coconut_count) * self.rate
        else:
            self.amount = Decimal('0.00')

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Employeecount ID: {self.id} - Coconut Count: {self.coconut_count}"  # Modified for clarity

       
        

      

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


class VendorPurchase(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    photo_upload = models.ImageField(upload_to='customer_photos/', blank=True, null=True)

    def __str__(self):
        return self.name 


class vendorsales(VendorPurchase,models.Model):
     date = models.DateTimeField(default=timezone.now) 
     coconut_kobbari = models.PositiveIntegerField()
     rate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
     amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
     
     def save(self, *args, **kwargs):
          if self.coconut_kobbari is not None and self.rate is not None:
            self.amount = self.coconut_kobbari * self.rate
          else:
            self.amount = 0
          super(vendorsales, self).save(*args, **kwargs)
         
         
   

    

  

    
   


