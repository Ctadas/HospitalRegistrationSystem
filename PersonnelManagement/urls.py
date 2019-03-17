from django.contrib import admin
from django.urls import path,include
from PersonnelManagement import views

urlpatterns = [
    path('getLoginCode/', views.getLoginCode,name = 'getLoginCode'),
    path('add_VisitCard/', views.add_VisitCard,name = 'add_VisitCard'),
    path('get_VisitCard/', views.get_VisitCard,name = 'get_VisitCard'),
    path('get_VisitCard_info/', views.get_VisitCard_info,name = 'get_VisitCard_info'),
    path('remove_VisitCard/', views.remove_VisitCard,name = 'remove_VisitCard')
]