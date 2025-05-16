from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def studentsView(request):
    students={'id': 1, 'name': 'John Doe', 'age': 25 }
    return JsonResponse(students)