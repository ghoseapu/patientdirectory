# This file defines URL patterns along with request functions in the Views.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_intro, name='intro'),
    path('patients/', views.view_patient_list, name='patient_list'),
    path('patients/<uuid:id>', views.view_single_patient, name='single_patient'),
]
