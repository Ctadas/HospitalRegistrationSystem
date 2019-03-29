from django.contrib import admin
from News.models import News,CarouselMap

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	#显示字段
	list_display = ('id', 'title', 'source', 'release_time')
	#可跳转字段
	list_display_links = ('id', 'title', 'source', 'release_time')
	#过滤器字段
	list_filter =('release_time','source') 
	#可搜索字段
	search_fields =('title', 'source', 'release_time')
	#每页显示条数
	list_per_page = 50

class CarouselMapAdmin(admin.ModelAdmin):
	#显示字段
	list_display = ('id', 'theme')
	#可跳转字段
	list_display_links = ('id', 'theme')
	#可搜索字段
	search_fields =('theme',)
	#每页显示条数
	list_per_page = 50

admin.site.register(News, NewsAdmin)
admin.site.register(CarouselMap, CarouselMapAdmin)