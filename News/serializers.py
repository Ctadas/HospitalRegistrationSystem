from rest_framework import serializers
from News.models import News,CarouselMap

class NewsSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = News
		fields = ('id','title','introduction','content','image','source','release_time')

class CarouselMapSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CarouselMap
		fields = ('id','theme','image')

