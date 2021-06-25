from django.contrib import admin
from django.urls import path
from datawork import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('apply/', views.apply, name="apply"),
    path('student/login/', views.student_login, name="student_login"),
    path('student/logout/', views.logout, name="student_logout"),
    path('student/dashboard/', views.student_dashboard, name="student_dashboard"),
    path('student/payment/', views.student_payment, name="student_payment"),
    path('student/payment/<int:pay_id>/done', views.payment_done, name="student_payment_done"),
    path('student/course/', views.student_course, name="student_course"),
    path('student/setting/', views.student_setting, name="student_setting"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
