from django.shortcuts import render, redirect
from django.contrib import messages
from .forms_students import UserRegisterForm as stud_reg
from .forms_teachers import UserRegisterForm as teacher_reg
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from .models import Teacher, Student, User


def register_stud(request):
    if request.method == 'POST':
        form = stud_reg(request.POST)
        if form.is_valid():
            form.save()
            #User == get_user_model()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = stud_reg()
    return render(request, 'users/student.html', {'form': form})


def register_teacher(request):
    if request.method == 'POST':
        form = teacher_reg(request.POST)
        if form.is_valid():
            form.save()
            #User == form.cleaned_data.get('User')
            #User == get_user_model()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = teacher_reg()
    return render(request, 'users/teacher.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def user_type(request):
    return render(request, 'users/user_type.html')


def public_teacher(request):
    teacher = User.objects.filter(is_teacher=1)
    teacher_a = Teacher.objects.all()
    context = {'teacher': teacher, 'teacher_a': teacher_a}
    return render(request, 'users/public_teacher.html', context)















