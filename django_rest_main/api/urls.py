from django.urls import path,include
from . import views
urlpatterns=[
    path('students', views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    path('employees/',views.Employees.as_view(),name='employees'),
    #path('employees/<int:pk>',views.Employees_obj.as_view(),name='employees_obj'),
]