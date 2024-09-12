from rest_framework import serializers
from main.models import Employee, Position, Shift, StaffShift, StaffAttendance

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['username', 'first_name', 'last_name', 'age', 'monthly_salary', 'workplace', 'phone_number', 'position']


class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = '__all__'


class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = ['staff', 'date', 'status']
        read_only_fields = ['status'] 
