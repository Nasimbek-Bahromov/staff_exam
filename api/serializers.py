from rest_framework import serializers
from main.models import Employee, StaffShift, StaffAttendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = '__all__'

class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = '__all__'
