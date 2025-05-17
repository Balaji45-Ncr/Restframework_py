from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeesViewSet,basename='employees')
router.register('employee_list',views.ModelViewset,basename='employees_list')


urlpatterns=[
    path('students', views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),

    # path('employees/',views.Employees.as_view(),name='employees'),
    # path('employees/<int:pk>',views.Employees_obj.as_view(),name='employees_obj'),
    path('',include(router.urls)),
    path('blogs/',views.BlogView.as_view()),
    path('comments/',views.CommentsView.as_view())


]