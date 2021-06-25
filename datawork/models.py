from django.db import models
from django.utils import timezone

# Create your models here.


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length=200)
    course_duration = models.CharField(max_length=200)
    course_fees = models.IntegerField()
    course_desc = models.TextField()

    def __str__(self):
        return self.course_title


class Student(models.Model):
    roll = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    dp = models.ImageField(upload_to="student/")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    dob = models.DateField()
    status = models.IntegerField(default=0)
    date_of_creation = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class StudentCourse(models.Model):
    studentCourse_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    type = models.IntegerField()

    def __str__(self):
        return self.course_id.course_title


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    payment_student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    MONTHS = (("1","Jan"),("2","Feb"),("3","March"),("4","Apr"),("5","May"),("6","June"),("7","July"),
              ("8","Aug"),("9","Sep"),("10","Oct"),("11","Nov"),("12","Dec"))
    payment_month = models.CharField(max_length=200,choices=MONTHS)
    payment_amount = models.IntegerField()
    payment_status = models.IntegerField(default=0)
    payment_doc = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.payment_student_id.full_name
