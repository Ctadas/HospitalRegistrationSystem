from django.db import models

# Create your models here.
#性别选择
job_title = (
	('主任医师','主任医师'),
	('副主任医师','副主任医师'),
	('主治医师','主治医师'),
	('医师','医师')
)

#上传头像目录定制
def upload_to(instance, filename):
	return '/'.join(['avatar', instance.name ,filename])

#就诊卡模型
class VisitCard(models.Model):
	real_name = models.CharField(verbose_name='真实姓名',max_length=50)
	id_card = models.CharField(verbose_name='身份证号码',max_length=18)
	id_type = models.CharField(verbose_name='证件类型',max_length=5)
	telphone = models.BigIntegerField(verbose_name='手机号码')

	def __str__(self):
		return self.real_name 

	class Meta:
		verbose_name = '就诊卡管理'
		verbose_name_plural = "就诊卡管理"

#医生信息模型
class DoctorInformation(models.Model):
	name = models.CharField(verbose_name='医生姓名',max_length=50)
	job_title = models.CharField(verbose_name='医生职称',max_length=30,choices=job_title)
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
	visit_card = models.ManyToManyField(VisitCard,blank=True,verbose_name='绑定就诊卡')

	def __str__(self):
		return self.openid 

	class Meta:
		verbose_name = '患者微信信息管理'
		verbose_name_plural = "患者微信信息管理"

