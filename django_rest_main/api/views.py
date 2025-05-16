from django.shortcuts import render
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
