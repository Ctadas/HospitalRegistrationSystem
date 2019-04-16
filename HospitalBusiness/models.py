from django.db import models
from django.db.models.signals import post_delete,post_save,m2m_changed
from django.dispatch import receiver
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

#挂号记录模型
class RegisteredRecord(models.Model):
	# wx_id = models.ForeignKey(PatientInformation,on_delete=models.CASCADE,verbose_name='操作微信号')
	department = models.ForeignKey(Department,on_delete=models.CASCADE,verbose_name='所属科室')
	registered_date = models.DateField(verbose_name = "挂号时间")
	visit_card = models.ForeignKey(VisitCard,on_delete=models.CASCADE,verbose_name='绑定就诊卡')
	doctors = models.ForeignKey(DoctorInformation,on_delete=models.CASCADE,verbose_name='就诊医生')
	submission_time = models.DateField(auto_now_add=True,verbose_name = "提交时间")

	def __str__(self):
		return str(self.submission_time)+','+self.visit_card.real_name

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

#值班时间模型
class Shift(models.Model):
	time = models.DateField(unique=True,verbose_name = "值班时间")
	doctor_duty = models.ManyToManyField(DoctorInformation,verbose_name='值班医生')

	def __str__(self):
		return str(self.time) 

	class Meta:
		verbose_name = '值班管理'
		verbose_name_plural = "值班管理"

#医生就诊次数管理
class DoctorVisitsNumber(models.Model):
	doctor = models.ForeignKey(DoctorInformation,verbose_name='医生名称',on_delete=models.CASCADE)
	visit_time = models.DateField(verbose_name='当天值班时间')
	visit_number = models.IntegerField(verbose_name='剩余就诊次数',default=30)
	association_registered_record = models.ManyToManyField(RegisteredRecord,blank=True,verbose_name='关联的挂号记录')

	def __str__(self):
		return self.doctor.name


	class Meta:
		verbose_name = '医生就诊次数管理'
		verbose_name_plural = "医生就诊次数管理"


#缴费项目管理
class PaymentItem(models.Model):
	name = models.CharField(verbose_name="项目名称",max_length=100)
	price = models.FloatField(verbose_name="项目金额",max_length=50)

	def __str__(self):
		return self.name  

	class Meta:
		verbose_name = '缴费项目管理'
		verbose_name_plural = "缴费项目管理"

#患者缴费管理
class Payment(models.Model):
	visit_card = models.ForeignKey(VisitCard,on_delete=models.CASCADE,verbose_name="患者就诊卡")
	payment_item = models.ManyToManyField(PaymentItem,verbose_name="缴费项目")

	def __str__(self):
		return self.visit_card.real_name  

	class Meta:
		verbose_name = '患者缴费管理'
		verbose_name_plural = "患者缴费管理"
	#定义放回值
	@property
	def visit_card_obj(self):
		visit_card_dict = {}
		visit_card_dict['real_name'] = self.visit_card.real_name
		visit_card_dict['id_card'] = self.visit_card.id_card
		visit_card_dict['id_type'] = self.visit_card.id_type
		visit_card_dict['telphone'] = self.visit_card.telphone
		return visit_card_dict

#就诊报告管理
class Report(models.Model):
	visit_card = models.ForeignKey(VisitCard,on_delete=models.CASCADE,verbose_name="患者就诊卡")
	report_content = models.TextField(verbose_name='报告内容',max_length=500)
	doctors = models.ForeignKey(DoctorInformation,on_delete=models.CASCADE,verbose_name='就诊医生')
	submission_time = models.DateField(auto_now_add=True,verbose_name = "报告生成时间")


	def __str__(self):
		return self.visit_card.real_name  

	class Meta:
		verbose_name = '就诊报告管理'
		verbose_name_plural = "就诊报告管理"

	#定义放回值
	@property
	def visit_card_obj(self):
		visit_card_dict = {}
		visit_card_dict['real_name'] = self.visit_card.real_name
		visit_card_dict['id_card'] = self.visit_card.id_card
		visit_card_dict['id_type'] = self.visit_card.id_type
		visit_card_dict['telphone'] = self.visit_card.telphone
		return visit_card_dict
	#定义放回值
	@property
	def doctors_obj(self):
		doctors_dict = {}
		doctors_dict['name'] = self.doctors.name
		doctors_dict['job_title'] = self.doctors.job_title
		return doctors_dict

@receiver(m2m_changed, sender=Shift.doctor_duty.through)
def create_visits_number(sender, instance,action, **kwargs):
	if action == 'post_add':
		visit_time = instance.time
		for doctor in instance.doctor_duty.all():
			doctor_visits_number = DoctorVisitsNumber.objects.filter(doctor = doctor,visit_time = visit_time)
			if doctor_visits_number.exists():
				pass
			else:
				DoctorVisitsNumber.objects.create(doctor = doctor,visit_time = visit_time)