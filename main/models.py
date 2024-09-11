from django.contrib.auth.models import AbstractUser
from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class Employee(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    workplace = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.ForeignKey(Position, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_shifts(self):
        # Xodimga tegishli shiftlarni olish
        shifts = StaffShift.objects.filter(staff=self).select_related('shift')
        return shifts

    def display_shifts(self):
        shifts = self.get_shifts()
        return [f"Shift from {shift.shift.start_time} to {shift.shift.end_time} on {shift.date}" for shift in shifts]
 



class StaffShift(models.Model):
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE)  
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)  
    date = models.DateField()

    def __str__(self):
        return f"{self.staff.get_full_name()} - {self.shift} on {self.date}"


class StaffAttendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ]
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    date = models.DateField()
    status = models.CharField(max_length=20, choices=ATTENDANCE_CHOICES)

    class Meta:
        unique_together = ('staff', 'date') 

    def __str__(self):
        return f"{self.staff.get_full_name()} - {self.date} - {self.status}"

