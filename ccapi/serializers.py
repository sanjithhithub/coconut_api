from rest_framework import serializers
from .models import EmployeeDetails, Employee
from .models import CustomerDetail
from .models import CustomerPurchase

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = ['id', 'name', 'mobile_number', 'photos', 'employee', 'coconut_count', 'rate', 'amount', 'date']
        read_only_fields = ['coconut_count', 'rate', 'amount', 'date']  # Added commas

    def validate_rate(self, value):
        if isinstance(value, list):
            raise serializers.ValidationError("Rate must be a single decimal number, not a list.")
        return value

    def validate(self, data):
        return data

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = ['id', 'name', 'mobile_number', 'address', 'photo_upload']

class CustomerPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPurchase
        fields = ['date', 'coconut_count', 'rate', 'amount']
       # read_only_fields = ['amount']  

    def validate(self, data):
       
        if data.get('coconut_count') is None:
            raise serializers.ValidationError({'coconut_count': 'This field is required.'})
        if data.get('rate') is None:
            raise serializers.ValidationError({'rate': 'This field is required.'})
        return data
