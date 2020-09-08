from django.shortcuts import render
from django.http import JsonResponse

from .models import Student
# Create your views here.

class StudentsVewSet(ModelViewSet):
  queryset = Student.objects.all()

def index(request):
  # list(Students.objects.values())
  # students = Student.objects.all()
  
  students = []
  for student in Student.objects.all():
    students.append({
      'name':student.name,
      'course':student.course,
      'rating':student.rating,
    })
  
  
  return JsonResponse(str(students),safe=False)