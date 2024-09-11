from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Employee, Position


@login_required
def dashboard(request):
    current_user = request.user
    if current_user.is_superuser:
        staff_members = Employee.objects.all()
    else:
        staff_members = Employee.objects.exclude(username=current_user.username)

    return render(request, 'dashboard/index.html', {'staff_members': staff_members})