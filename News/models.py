from django.db import models

# Create your models here.
#新闻模型
class News(models.Model):
	title = models.CharField(verbose_name='新闻标题',max_length=100)
	introduction = models.TextField(verbose_name='新闻简介',max_length=500)
	content = models.TextField(verbose_name='新闻内容',max_length=5000)
	image = models.ImageField(verbose_name='新闻图片',upload_to='news/%Y/%m/%d/')
	source = models.CharField(verbose_name='新闻来源',max_length=50)
	release_time = models.DateField(verbose_name='发布时间',auto_now_add = True)

	def __str__(self):
		return self.title 

	class Meta:
		verbose_name = '新闻管理'
		verbose_name_plural = "新闻管理"

#轮播图模型
class CarouselMap(models.Model):
	theme = models.CharField(verbose_name='轮播图片主题',max_length=100)
	image = models.ImageField(verbose_name='轮播图片',upload_to='CarouselMap/%Y/%m/%d/')

	def __str__(self):
		return self.theme

	class Meta:
		verbose_name = '轮播图'
		verbose_name_plural = "轮播图"