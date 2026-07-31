from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
  class Meta:
   model = Student
   fields = ['full_name', 'age', 'bio', 'cours']
   read_only_fields = ['create_at']
