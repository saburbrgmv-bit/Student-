from django.db import models

class Student(models.Model):
  full_name = models.CharField(max_length=150)
  age = models.IntegerField()
  bio = models.TextField()
  cours = models.CharField(max_length=50)
  create_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.full_name
