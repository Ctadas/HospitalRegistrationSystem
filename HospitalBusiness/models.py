from django.db import models
from PersonnelManagement.models import DoctorInformation,PatientInformation

# Create your models here.
#科室类别模型
class DepartmentClassification(models.Model):
	name = models.CharField(verbose_name='科室类别名称',max_length=50)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = '科室类别管理'
		verbose_name_plural = "科室类别管理"

#科室模型
class Department(models.Model):
	name = models.CharField(verbose_name='科室名称',max_length=50)
	category = models.ForeignKey(DepartmentClassification,on_delete=models.CASCADE,verbose_name='所属科室类别')
	doctors = models.ManyToManyField(DoctorInformation,verbose_name='科室所属医生')

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = '科室管理'
		verbose_name_plural = "科室管理"

#就诊卡模型
class VisitCard(models.Model):
	user = models.ManyToManyField(PatientInformation)
	real_name = models.CharField(verbose_name='真实姓名',max_length=50)
	id_card = models.CharField(verbose_name='身份证号码',max_length=18)
	telphone = models.BigIntegerField(verbose_name='手机号码')

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = '就诊卡管理'
		verbose_name_plural = "就诊卡管理"
