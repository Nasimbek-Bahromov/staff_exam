from django.urls import path, include
from dashboard import views
from .views import login_view, logout_view, staff_create, staff_update,staff_delete

app_name = 'dashboard'
urlpatterns = [
    path('staff/', views.staffList, name = 'staff-list'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('staff/create/', staff_create, name='staff-create'),
    path('staff/update/<int:id>/', staff_update, name='staff-update'),
    path('staff/<int:id>/delete/', staff_delete, name='staff-delete'),
    path('attendance/start/', views.attendance_start, name='attendance_start'),
    path('attendance/', views.attendance_list, name='attendance_list'),
]

