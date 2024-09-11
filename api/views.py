from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Employee, StaffShift, StaffAttendance
from .serializers import EmployeeSerializer, StaffShiftSerializer, StaffAttendanceSerializer

class EmployeeListCreate(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)
        if employee is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        if employee is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        if employee is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StaffShiftListCreate(APIView):
    def get(self, request):
        shifts = StaffShift.objects.all()
        serializer = StaffShiftSerializer(shifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffShiftDetail(APIView):
    def get_object(self, pk):
        try:
            return StaffShift.objects.get(pk=pk)
        except StaffShift.DoesNotExist:
            return None

    def get(self, request, pk):
        shift = self.get_object(pk)
        if shift is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StaffShiftSerializer(shift)
        return Response(serializer.data)

    def put(self, request, pk):
        shift = self.get_object(pk)
        if shift is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StaffShiftSerializer(shift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shift = self.get_object(pk)
        if shift is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StaffAttendanceListCreate(APIView):
    def get(self, request):
        attendances = StaffAttendance.objects.all()
        serializer = StaffAttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffAttendanceDetail(APIView):
    def get_object(self, pk):
        try:
            return StaffAttendance.objects.get(pk=pk)
        except StaffAttendance.DoesNotExist:
            return None

    def get(self, request, pk):
        attendance = self.get_object(pk)
        if attendance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StaffAttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        attendance = self.get_object(pk)
        if attendance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StaffAttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attendance = self.get_object(pk)
        if attendance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)