from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeDetailUpdateDeleteView.as_view(), name='employee-detail-update-delete'),
    path('positions/', views.PositionListCreateView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', views.PositionDetailUpdateDeleteView.as_view(), name='position-detail-update-delete'),
    path('shifts/', views.ShiftListCreateView.as_view(), name='shift-list-create'),
    path('shifts/<int:pk>/', views.ShiftDetailUpdateDeleteView.as_view(), name='shift-detail-update-delete'),
    path('staff-shifts/', views.StaffShiftListCreateView.as_view(), name='staffshift-list-create'),
    path('staff-shifts/<int:pk>/', views.StaffShiftDetailUpdateDeleteView.as_view(), name='staffshift-detail-update-delete'),
    path('attendances/', views.StaffAttendanceListView.as_view(), name='attendance-list'),
]
