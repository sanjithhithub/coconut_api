from rest_framework import serializers
from .models import EmployeeDetails, Employee

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = ['id', 'name', 'mobile_number', 'photos', 'employee', 'coconut_count', 'rate', 'amount', 'date']
        read_only_fields = ['coconut_count' 'rate', 'amount', 'date']

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
