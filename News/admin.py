from django.contrib import admin
from News.models import News,CarouselMap

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	pass

class CarouselMapAdmin(admin.ModelAdmin):
	 # list_display = ('id', 'title', 'release_time','visits')

	 # list_display_links = ('id', 'title')
	 pass

admin.site.register(News, NewsAdmin)
admin.site.register(CarouselMap, CarouselMapAdmin)