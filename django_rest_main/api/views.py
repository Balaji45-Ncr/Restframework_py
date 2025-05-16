from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
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

