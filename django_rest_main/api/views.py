from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
@api_view(['GET','POST'])
def studentsView(request):
    if request.method=='GET':
    # try:
        students=Student.objects.all()
        #a=serializers.serialize(students)
        a=StudentSerializer(students,many=True)
        return Response(a.data,status=status.HTTP_200_OK)
    # except TypeError:
    #     return HttpResponse('<h1>sorry type error</h1>')
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['PUT','PATCH','GET'])
def studentDetailView(request,pk):
    try:
        model_data=get_object_or_404(Student,pk=pk)
        #modified_data=StudentSerializer(model_data,data=request.data)
       # if modified_data.is_valid():
          #  modified_data.save()
          # # serializer=StudentSerializer(model_data)
            #return Response(modified_data.data,status=status.HTTP_200_OK)
    except :
        return Response({'message':'Sorry not found'},status=status.HTTP_400_BAD_REQUEST)

    if request.method =='GET':
        #student_data=Student.objects.all()
        serializer=StudentSerializer(model_data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PATCH':
        serializers=StudentSerializer(model_data,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
    else:
        serializers = StudentSerializer(model_data, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class Employees(APIView):
    def get(self,request,*args,**kwargs):
        employee=Employee.objects.all()
        serializer=EmployeeSerializer(employee,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        post_data=EmployeeSerializer(data=request.data)
        if post_data.is_valid():
            post_data.save()
            return Response(post_data.data,status=status.HTTP_201_CREATED)
class Employees_obj(APIView):
    def get_object(self,request,pk):
        try:
            employee_data=Employee.objects.get(pk=pk)
            return employee_data
        except Employee.MultipleObjectsReturned:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def get(self,request,pk,*args,**kwargs):
    #     emp_data=self.get_object(request,pk)
    #     if isinstance(emp_data,Response):
    #         return emp_data
    #     serializer=EmployeeSerializer(emp_data)
    #     return Response(serializer.data,status=status.HTTP_200_OK)

    def get(self,request,pk,*args,**kwargs):
        emp_data=self.get_object(request,pk)
        if isinstance(emp_data,Response):
            return emp_data
        serializer=EmployeeSerializer(emp_data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk,*args,**kwargs):
        emp_data = self.get_object(request, pk)
        serializer=EmployeeSerializer(emp_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,*args,**kwargs):
        emp_data=self.get_object(request,pk)
        emp_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



