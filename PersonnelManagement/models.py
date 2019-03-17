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

#就诊卡模型
class VisitCard(models.Model):
	real_name = models.CharField(verbose_name='真实姓名',max_length=50)
	id_card = models.CharField(verbose_name='身份证号码',max_length=18)
	id_type = models.CharField(verbose_name='身份证类型',max_length=5)
	telphone = models.BigIntegerField(verbose_name='手机号码')

	def __str__(self):
		return self.real_name 

	class Meta:
		verbose_name = '就诊卡管理'
		verbose_name_plural = "就诊卡管理"

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
	openid = models.CharField(verbose_name='用户唯一标识',max_length=50)
	session_key = models.CharField(verbose_name='会话秘钥',max_length=50)
	visit_card = models.ManyToManyField(VisitCard,blank=True)

	def __str__(self):
		return self.openid 

	class Meta:
		verbose_name = '患者微信信息管理'
		verbose_name_plural = "患者微信信息管理"

