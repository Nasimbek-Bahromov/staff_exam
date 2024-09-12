from rest_framework import generics, permissions
from main.models import Employee, Position, Shift, StaffShift, StaffAttendance
from .serializers import EmployeeSerializer, PositionSerializer, ShiftSerializer, StaffShiftSerializer, StaffAttendanceSerializer

# Staff (Employee) uchun 
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

# Position uchun 
class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]

class PositionDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]

# Shift uchun 
class ShiftListCreateView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShiftDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [permissions.IsAuthenticated]

# StaffShift uchun 
class StaffShiftListCreateView(generics.ListCreateAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [permissions.IsAuthenticated]

class StaffShiftDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer
    permission_classes = [permissions.IsAuthenticated]

# StaffAttendance uchun (GET ONLY)
class StaffAttendanceListView(generics.ListAPIView):
    queryset = StaffAttendance.objects.all()
    serializer_class = StaffAttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
