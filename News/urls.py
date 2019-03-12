from django.contrib import admin
from django.urls import path
from News import views

urlpatterns = [
	path('news_list/',views.news_list,name='news_list'),
	path('carousel_map_list/',views.carousel_map_list,name='carousel_map_list'),
	path('get_news/',views.get_news,name='get_news')
]
