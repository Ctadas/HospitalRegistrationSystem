from django.contrib import admin
from django.urls import path,include
from HospitalBusiness import views

urlpatterns = [
    path('get_department_info/', views.get_department_info,name = 'get_department_info'),
    path('get_shift/', views.get_shift,name = 'get_shift'),
    path('commit_registered_record/', views.commit_registered_record,name = 'commit_registered_record'),
    path('get_registered_record/', views.get_registered_record,name = 'get_registered_record'),
]