from django.urls import path
from .views import *

urlpatterns = [
  path('student/', all_read),
  path('student/create', all_create),
  path('student/update', all_update),
  path('student/delete', all_delete),

]