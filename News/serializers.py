from rest_framework import serializers
from News.models import News,CarouselMap

class NewsSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = News
		fields = ('title','content','image','source','release_time')

class CarouselMapSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CarouselMap
		fields = ('theme','image')

