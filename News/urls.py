from django.contrib import admin
from django.urls import path
from News.views import news_list,carousel_map_list

urlpatterns = [
	path('news_list/',news_list,name='news_list'),
	path('carousel_map_list/',carousel_map_list,name='carousel_map_list')
]
