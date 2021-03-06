from django.shortcuts import render
from News.models import News,CarouselMap
from News.serializers import NewsSerializers,CarouselMapSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
# Create your views here.
#获取新闻列表
@api_view(['GET'])
def news_list(request):
	if request.method == 'GET':
		news = News.objects.all().order_by('-release_time')[0:5]
		serializer = NewsSerializers(news, many=True)
		return Response(serializer.data)

#获取新闻轮播
@api_view(['GET'])
def carousel_map_list(request):
	if request.method == 'GET':
		carousel_map = CarouselMap.objects.all()
		serializer = CarouselMapSerializers(carousel_map, many=True)
		return Response(serializer.data)

#获取新闻详细内容
@api_view(['GET'])
def get_news(request):
	news_id = request.GET.get('id')
	if request.method == 'GET':
		news = News.objects.filter(id = news_id)
		serializer = NewsSerializers(news, many=True)
		return Response(serializer.data)
