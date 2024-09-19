from django.utils import timezone
from decimal import Decimal, InvalidOperation
from django.db import models


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

        # Calculate the amount based on coconut_count and rate
        if self.coconut_count and self.rate:
            self.amount = Decimal(self.coconut_count) * self.rate
        else:
            self.amount = Decimal('0.00')

        # Ensure that `date` is always a date, not datetime
        if isinstance(self.date, timezone.datetime):
            self.date = self.date.date()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.employee.name}"
