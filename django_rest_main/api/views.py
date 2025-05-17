from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from students.models import Student
from employees.models import Employee
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin
from rest_framework.views import APIView
from rest_framework import generics
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from blogs.models import Blog,Comment
from blogs.serializers import CommentSerializer,BlogSerializer

from rest_framework.decorators import action
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

# class Employees(APIView):
#     def get(self,request,*args,**kwargs):
#         employee=Employee.objects.all()
#         serializer=EmployeeSerializer(employee,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request,*args,**kwargs):
#         post_data=EmployeeSerializer(data=request.data)
#         if post_data.is_valid():
#             post_data.save()
#             return Response(post_data.data,status=status.HTTP_201_CREATED)
# class Employees_obj(APIView):
#     def get_object(self,request,pk):
#         try:
#             employee_data=Employee.objects.get(pk=pk)
#             return employee_data
#         except Employee.MultipleObjectsReturned:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         except Employee.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     # def get(self,request,pk,*args,**kwargs):
#     #     emp_data=self.get_object(request,pk)
#     #     if isinstance(emp_data,Response):
#     #         return emp_data
#     #     serializer=EmployeeSerializer(emp_data)
#     #     return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def get(self,request,pk,*args,**kwargs):
#         emp_data=self.get_object(request,pk)
#         if isinstance(emp_data,Response):
#             return emp_data
#         serializer=EmployeeSerializer(emp_data)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def put(self,request,pk,*args,**kwargs):
#         emp_data = self.get_object(request, pk)
#         serializer=EmployeeSerializer(emp_data,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,*args,**kwargs):
#         emp_data=self.get_object(request,pk)
#         emp_data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


'''

Mixins:


Mixins are reusable code classes in oops that provide specific functionalities

In django rest framework, mixins are used to add common functionalities to views

create,read,update and delete operations

ListModelMixin         ------------------->list() - once u extend this listmodelmixin into your cbv you have support for returning list of objects automatically and also provide built in method called list()
RetrieveModelMixin     -------------------> retrieve()
CreateModelMixin       ------------------->create()
UpdateModelMixin       ------------------->update()
DestroyModelMixin      ------------------->destroy()


syntax: class Employees(mixins,generics.GenericAPIView)

generics acts as foundational class for building most api views and essentials functionalities for handling http request(get,put,post,delete)

request handling and response generation was taken care by generics and core functionalities of crud taken care by mixins
'''
# class Employees(ListModelMixin,CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
# class Employees_obj(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def get(self,request,pk,*args,**kwargs):
#         return self.retrieve(request,pk=pk,*args,**kwargs)
#     def put(self,request,pk,*args,**kwargs):
#         return self.update(request,pk=pk,*args,**kwargs)
#
#     def delete(self,request,pk,*args,**kwargs):
#         return self.destroy(request,pk=pk,*args,**kwargs)

'''
Generics

ListAPIView
CreateAPIView
RetrieveAPIView
UpdateAPIView
DestroyAPIView

ListCreateAPIView
RetrieveUpdateAPIView
RetrieveUpdate DestroyAPIView
'''
class Employees(generics.CreateAPIView,generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # def list(self, request, *args, **kwargs):
    #     self.list(request,*args,**kwargs)
    # def create(self, request, *args, **kwargs):
class Employees_obj(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

'''
Viewsets:

viewsets.ViewSet ------------> list(),create(),retrieve(),update(),delete()

viewsets.ModelViewSet -------> Takes onyl queryset and serializer_class and automatically provides both pk based and non-pk based operations

'''
class EmployeesViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Employee.objects.all()
        serializers= EmployeeSerializer(queryset,many=True)
        return Response(serializers.data)
    def create(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def retrieve(self,request,pk=None):
        employee=get_object_or_404(Employee,pk=pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data)


class ModelViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
