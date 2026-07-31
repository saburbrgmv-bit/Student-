from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def all_read(request):
  student = Student.objects.all()
  serializers = StudentSerializers(student, many=True)
  return Response(serializers, status=status.HTTP_200_OK)

@api_view(['POST'])
def all_create(request):
  serializers = StudentSerializers(data=request.data)
  if serializers.is_valid():
    serializers.save()
    return Response(serializers.data, status=status.HTTP_201_CREATED)
  return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def all_update(request, id):
  student = get_object_or_404(Student, id=id)
  serializers = StudentSerializers(student, data=request.data)
  if serializers.is_valid():
    serializers.save()
    return Response(serializers.data, status=status.HTTP_200_OK)
  return Response(serializers.errors)

@api_view(['DELETE'])
def all_delete(request, id):
  student = get_object_or_404(Student, id=id)
  student.delete()
  return Response(student, status=status.HTTP_204_NO_CONTENT)
