from django.db import models

# Create your models here.
#性别选择
gender_choices = (
	('man','男'),
	('woman','女')
)

#上传头像目录定制
def upload_to(instance, filename):
	return '/'.join(['avatar', instance.name ,filename])

#医生信息模型
class DoctorInformation(models.Model):
	name = models.CharField(verbose_name='医生姓名',max_length=50)
	gender = models.CharField(verbose_name='医生性别',max_length=10,choices=gender_choices)
	doctor_introduction = models.TextField(verbose_name='医生介绍',max_length=500)
	avatar = models.ImageField(verbose_name='医生头像',upload_to=upload_to)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = '医生信息管理'
		verbose_name_plural = "医生信息管理"

#患者信息模型
class PatientInformation(models.Model):
	name = models.CharField(verbose_name='用户名',max_length=50)
	avatar = models.ImageField(verbose_name='头像',upload_to=upload_to)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = '患者信息管理'
		verbose_name_plural = "患者信息管理"