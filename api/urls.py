from django.urls import path
from .views import (
    EmployeeListCreate, EmployeeDetail,
    StaffShiftListCreate, StaffShiftDetail,
    StaffAttendanceListCreate, StaffAttendanceDetail
)

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    
    path('staff-shifts/', StaffShiftListCreate.as_view(), name='staff-shift-list-create'),
    path('staff-shifts/<int:pk>/', StaffShiftDetail.as_view(), name='staff-shift-detail'),
    
    path('staff-attendances/', StaffAttendanceListCreate.as_view(), name='staff-attendance-list-create'),
    path('staff-attendances/<int:pk>/', StaffAttendanceDetail.as_view(), name='staff-attendance-detail'),
]
