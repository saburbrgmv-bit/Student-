from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
  class Meta:
   model = Student
   fields = ['full_name', 'age', 'number']

  def validate_age(self, value):
    if value < 18:
      raise serializers.ValidationError('kirish mumkin emas')
    return value

  def validate_number(self, value):
    if not value.startswith("+998"):
      raise serializers.ValidationError('boshi +998 bn kiriting')
    return value
