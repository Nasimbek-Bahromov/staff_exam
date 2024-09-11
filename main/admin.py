from django.contrib import admin
from .models import Employee, Position, Shift, StaffShift, StaffAttendance

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'age', 'monthly_salary', 'workplace', 'phone_number', 'position')
    search_fields = ('username', 'first_name', 'last_name', 'phone_number', 'position__name')
    list_filter = ('position', 'age')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',) 

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')
    search_fields = ('start_time', 'end_time')
    list_filter = ('start_time', 'end_time') 

class StaffShiftAdmin(admin.ModelAdmin):
    list_display = ('staff', 'shift', 'date')
    search_fields = ('staff__username', 'shift__start_time', 'shift__end_time', 'date') 
    list_filter = ('staff', 'shift', 'date')  

class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff', 'date', 'status')
    search_fields = ('staff__username', 'date', 'status') 
    list_filter = ('status', 'date') 

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(StaffShift, StaffShiftAdmin)
admin.site.register(StaffAttendance, StaffAttendanceAdmin)
