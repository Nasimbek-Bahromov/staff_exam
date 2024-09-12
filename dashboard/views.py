from django.shortcuts import render,redirect
from main.models import Employee, Position, Shift, StaffShift,StaffAttendance
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone

@login_required
def staffList(request):
    current_user = request.user
    if current_user.is_superuser:
        staff_members = Employee.objects.all()
    else:
        staff_members = Employee.objects.exclude(username=current_user.username)

    return render(request, 'dashboard/staff-list.html', {'staff_members': staff_members})


@login_required
def staff_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        monthly_salary = request.POST.get('monthly_salary')
        workplace = request.POST.get('workplace')
        phone_number = request.POST.get('phone_number')
        position_id = request.POST.get('position')
        shift_ids = request.POST.getlist('shift')

        position_instance = Position.objects.filter(id=position_id).first()

        if position_instance is None:
            messages.error(request, 'Noto\'g\'ri pozitsiya tanlandi.')
            return render(request, 'dashboard/staff-create.html', {
                'title': "Xodim yaratish",
                'positions': Position.objects.all(),
                'shifts': Shift.objects.all(),
            })

    
        username = (first_name + last_name).lower()
        existing_user = Employee.objects.filter(username=username).exists()
        if existing_user:
            messages.error(request, 'Bunday username bilan xodim mavjud.')
            return render(request, 'dashboard/staff-create.html', {
                'title': "Xodim yaratish",
                'positions': Position.objects.all(),
                'shifts': Shift.objects.all(),
            })

        try:
            employee = Employee.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                age=age,
                monthly_salary=monthly_salary,
                workplace=workplace,
                phone_number=phone_number,
                position=position_instance,
                password='password' 
            )
            
            for shift_id in shift_ids:
                shift = Shift.objects.get(id=shift_id)
                StaffShift.objects.create(staff=employee, shift=shift, date=datetime.date.today())
            
            messages.success(request, 'Xodim muvaffaqiyatli yaratildi.')
            return redirect('dashboard:staff-list')
        except Exception as e:
            messages.error(request, f'Xodimni yaratishda xatolik yuz berdi: {e}')

    positions = Position.objects.all()
    shifts = Shift.objects.all()

    context = {
        'title': "Xodim yaratish",
        'positions': positions,
        'shifts': shifts,
    }

    return render(request, 'dashboard/staff-create.html', context)


@login_required
def staff_update(request, id):
    employee = Employee.objects.filter(id=id).first()

    if not employee:
        messages.error(request, 'Xodim topilmadi.')
        return redirect('dashboard:staff-list')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        monthly_salary = request.POST.get('monthly_salary')
        workplace = request.POST.get('workplace')
        phone_number = request.POST.get('phone_number')
        position_id = request.POST.get('position')
        shift_ids = request.POST.getlist('shift')

        position_instance = Position.objects.filter(id=position_id).first()

        if position_instance is None:
            messages.error(request, 'Noto\'g\'ri pozitsiya tanlandi.')
            return render(request, 'dashboard/staff-update.html', {
                'title': "Xodimni yangilash",
                'employee': employee,
                'positions': Position.objects.all(),
                'shifts': Shift.objects.all(),
                'employee_shifts': StaffShift.objects.filter(staff=employee).values_list('shift_id', flat=True),
            })

        try:
            
            employee.first_name = first_name
            employee.last_name = last_name
            employee.age = age
            employee.monthly_salary = monthly_salary
            employee.workplace = workplace
            employee.phone_number = phone_number
            employee.position = position_instance
            employee.save()

            
            StaffShift.objects.filter(staff=employee).delete()
            for shift_id in shift_ids:
                try:
                    shift = Shift.objects.get(id=shift_id)
                    StaffShift.objects.create(staff=employee, shift=shift, date=datetime.date.today())
                except Shift.DoesNotExist:
                    messages.error(request, f"Shift {shift_id} topilmadi.")
                    return redirect('dashboard:staff-update', id=id)

            messages.success(request, 'Xodim muvaffaqiyatli yangilandi.')
            return redirect('dashboard:staff-list')
        except Exception as e:
            messages.error(request, f'Xodimni yangilashda xatolik yuz berdi: {e}')

    positions = Position.objects.all()
    shifts = Shift.objects.all()
    employee_shifts = StaffShift.objects.filter(staff=employee).values_list('shift_id', flat=True)

    context = {
        'title': "Xodimni yangilash",
        'employee': employee,
        'positions': positions,
        'shifts': shifts,
        'employee_shifts': employee_shifts,
    }

    return render(request, 'dashboard/staff-update.html', context)


@login_required
def attendance_start(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        attendance_data = request.POST.getlist('attendance_status')
        date = timezone.now().date()


        for i, employee_id in enumerate(request.POST.getlist('employee_id')):
            status = attendance_data[i]
            employee = Employee.objects.get(id=employee_id)
            
    
            attendance, created = StaffAttendance.objects.get_or_create(
                staff=employee,
                date=date,
                defaults={'status': status}
            )
            if not created:
                attendance.status = status
                attendance.save()

        return redirect('dashboard:attendance_list')

    context = {
        'employees': employees,
        'title': 'Davomatni Belgilash'
    }
    return render(request, 'dashboard/attendance_start.html', context)


@login_required
def attendance_list(request):
    attendances = StaffAttendance.objects.all().order_by('-date')
    context = {
        'attendances': attendances,
    }
    return render(request, 'dashboard/attendance_list.html', context)


@login_required
def staff_delete(request, id):
    try:
    
        staff = Employee.objects.get(id=id)
        staff.delete()
        messages.success(request, 'Xodim muvaffaqiyatli o\'chirildi.')
    except Employee.DoesNotExist:
        messages.error(request, 'Xodim topilmadi.')
    except Exception as e:
        messages.error(request, f'Xodimni o\'chirishda xatolik yuz berdi: {e}')
    
    return redirect('dashboard:staff-list')



User = get_user_model()
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:staff-list') 
        else:
            return render(request, 'dashboard/login.html', {'error': 'Invalid username or password'})
    return render(request, 'dashboard/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('dashboard:login')
