from rest_framework import serializers
from .models import EmployeeDetails,  CustomerDetail, CustomerPurchase, VendorPurchase, Employeecount,vendorsales


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = ['id', 'name', 'mobile_number', 'photos', 'date']  # Fixed 'Employee' to 'employee'


class EmployeecountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeecount
        fields = ['id','coconut_count', 'rate', 'amount']
        read_only_fields = ['amount']  # Mark 'rate' and 'amount' as read-only

    def validate_rate(self, value):
        if isinstance(value, list):
            raise serializers.ValidationError("Rate must be a single decimal number, not a list.")
        return value




class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = ['id', 'name', 'mobile_number', 'address', 'photo_upload']


class CustomerPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPurchase
        fields = ['date', 'coconut_count', 'rate', 'amount']
        read_only_fields = ['amount']

    def validate(self, data):
        # Custom validation if needed
        if data.get('coconut_count') is None:
            raise serializers.ValidationError({'coconut_count': 'This field is required.'})
        if data.get('rate') is None:
            raise serializers.ValidationError({'rate': 'This field is required.'})
        return data


class VendorPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPurchase
        fields = ['id', 'name', 'mobile_number', 'company_name', 'address', 'photo_upload']  


class vendorsalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendorsales
        fields = ['id', 'date', 'coconut_kobbari', 'rate', 'amount']  # Fixed the space after 'date'
        read_only_fields = ['amount']
