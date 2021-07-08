from rest_framework import serializers

from main.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['created_date', 'updated_date']
