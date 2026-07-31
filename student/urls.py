from django.urls import path
from .views import *

urlpatterns = [
  path('book/', all_read),
  path('book/create', all_create),
  path('book/update', all_update),
  path('book/delete', all_delete),

]