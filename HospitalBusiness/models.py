from django.db import models
from PersonnelManagement.models import DoctorInformation,PatientInformation,VisitCard

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

#值班时间模型
class Shift(models.Model):
	time = models.DateField(verbose_name = "值班时间")
	doctor_duty = models.ManyToManyField(DoctorInformation,verbose_name='值班医生')

	def __str__(self):
		return str(self.time) 

	class Meta:
		verbose_name = '值班管理'
		verbose_name_plural = "值班管理"

#挂号记录模型
class RegisteredRecord(models.Model):
	# wx_id = models.ForeignKey(PatientInformation,on_delete=models.CASCADE,verbose_name='操作微信号')
	department = models.ForeignKey(Department,on_delete=models.CASCADE,verbose_name='所属科室')
	registered_date = models.DateField(verbose_name = "挂号时间")
	visit_card = models.ForeignKey(VisitCard,on_delete=models.CASCADE,verbose_name='绑定就诊卡')
	doctors = models.ForeignKey(DoctorInformation,on_delete=models.CASCADE,verbose_name='就诊医生')
	submission_time = models.DateField(auto_now_add=True,verbose_name = "提交时间")

	def __str__(self):
		return str(self.submission_time) 

	class Meta:
		verbose_name = '挂号记录'
		verbose_name_plural = "挂号记录"

	@property
	def visit_card_obj(self):
		visit_card_dict = {}
		visit_card_dict['real_name'] = self.visit_card.real_name
		visit_card_dict['id_card'] = self.visit_card.id_card
		visit_card_dict['id_type'] = self.visit_card.id_type
		visit_card_dict['telphone'] = self.visit_card.telphone
		return visit_card_dict

	@property
	def doctors_obj(self):
		doctors_dict = {}
		doctors_dict['name'] = self.doctors.name
		doctors_dict['job_title'] = self.doctors.job_title
		return doctors_dict
