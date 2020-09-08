from rest_framework import ModelSerializer
from .models import Student

class StudentSerializer(ModelSerializer):
  class Meta:
    model = Student
    fields = ['id','name','course','rating']