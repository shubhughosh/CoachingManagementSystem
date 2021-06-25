from django.shortcuts import render, redirect
from .forms import *
from django.db.models import Q, Sum
# Create your views here.


def home(r):
    return render(r, 'home.html')


def apply(r):
    form = InsertStudent(r.POST or None, r.FILES or None)
    data = {"insert_form": form}
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(apply)
        else:
            return render(r, 'apply.html', data)
    return render(r, 'apply.html', data)


def student_login(r):
    if r.method == 'POST':
        email = r.POST.get('email')
        password = r.POST.get('password')
        condition = (Q(email=email) & Q(password=password))
        check = Student.objects.filter(condition).count()
        if check > 0:
            r.session['student_log'] = email
            return redirect(student_dashboard)
        else:
            return redirect(student_login)
    return render(r, 'login.html')


def student_dashboard(r):
    if not r.session.has_key('student_log'):
        return redirect(student_login)


    roll = (Student.objects.get(email=r.session['student_log'])).roll

    # checking course

    if StudentCourse.objects.filter(student_id=roll).exists()==False:
        alert = 1


#############
    cond = Q(payment_student_id=roll) & Q(payment_status=0)
    data = {
        "student": Student.objects.filter(roll =roll),
        'payment': Payment.objects.filter(payment_student_id=roll),
        'student_course': StudentCourse.objects.filter(student_id=roll),
        'due': Payment.objects.filter(cond).aggregate(Sum('payment_amount')),
        'emptycourse':alert
    }
    return render(r, 'student/student_dashboard.html',data)


def student_course(r):
    if not r.session.has_key('student_log'):
        return redirect(student_login)
    log = r.session['student_log']
    std = Student.objects.get(email=log).roll
    data = {
        'studentcourse': StudentCourse.objects.filter(student_id=std),
        'student':Student.objects.filter(roll=std)
    }
    return render(r,'student/student_course.html',data)


def student_payment(r):
    roll = (Student.objects.get(email=r.session['student_log'])).roll
    cond = Q(payment_student_id=roll) & Q(payment_status=0)
    data = {
        "student": Student.objects.filter(roll=roll),
        'payment': Payment.objects.filter(payment_student_id=roll),
        'student_course': StudentCourse.objects.filter(student_id=roll),
        'due': Payment.objects.filter(cond).aggregate(Sum('payment_amount'))
    }
    if not r.session.has_key('student_log'):
        return redirect(student_login)

    std = Student.objects.filter(email=r.session['student_log'])
    doa = std[0].date_of_creation.month
    current_month = timezone.now().month
    print(doa)
    for x in range(doa,current_month+1):
        if Payment.objects.filter(payment_month=x).exists()==False:
            p = Payment()
            p.payment_month = x
            p.payment_student_id = Student(std[0].roll)
            p.payment_amount = 700
            p.payment_doc = timezone.now()
            p.payment_status = 0
            p.save()

    return render(r, 'student/student_payment.html',data)


def student_setting(r):
    return render(r, 'student/student_setting.html')


def logout(r):
    if r.session.has_key('student_log'):
        del r.session['student_log']
    return redirect(student_login)


def payment_done(r, pay_id):
    p = Payment.objects.get(pay_id=pay_id)
    p.payment_status = 1
    p.save()
    return redirect(student_dashboard)