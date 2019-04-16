from django.contrib import admin
from HospitalBusiness.models import DepartmentClassification,Department,Shift,RegisteredRecord,PaymentItem,Payment,Report,DoctorVisitsNumber

# Register your models here.
class DoctorVisitsNumberAdmin(admin.ModelAdmin):
	list_display=('id','doctor','visit_time','visit_number')

	list_display_links = ('id','doctor','visit_time','visit_number')

	#多对多字段编辑
	filter_horizontal=('association_registered_record',)

class DepartmentClassificationAdmin(admin.ModelAdmin):
	list_display=('id','name',)

	list_display_links = ('id',)

	search_fields = ('name',)

	list_editable = ('name',)

	list_per_page = 50

class DepartmentAdmin(admin.ModelAdmin):
	#显示字段
	list_display = ('id', 'name', 'category','就诊医生')
	#可跳转字段
	list_display_links = ('id', 'name','就诊医生')
	#过滤器字段
	list_filter =('category',) 
	#可编辑字段
	list_editable = ('category',)
	#可搜索字段
	search_fields =('name','category__name','doctors__name')
	#每页显示条数
	list_per_page = 50
	#多对多字段编辑
	filter_horizontal=('doctors',)

	def 就诊医生(self,obj):
		return [doctor.name for doctor in  obj.doctors.all()]

class ShiftAdmin(admin.ModelAdmin):

	list_display = ('id', 'time', '值班医生',)
	#可跳转字段
	list_display_links = ('id', 'time','值班医生')
	#过滤器字段
	list_filter =('time',) 
	#可搜索字段
	search_fields =('name','值班医生')
	#每页显示条数
	list_per_page = 50
	#多对多字段编辑
	filter_horizontal=('doctor_duty',)

	def 值班医生(self,obj):
		return [doctor.name for doctor in  obj.doctor_duty.all()]

class RegisteredRecordAdmin(admin.ModelAdmin):
	list_display = ('id', 'department','registered_date','visit_card','doctors','submission_time')
	#可跳转字段
	list_display_links = ('id', 'department','registered_date','visit_card','doctors','submission_time')
	#过滤器字段
	list_filter =('registered_date','submission_time',) 
	#可搜索字段
	search_fields =('department__name','registered_date','visit_card__realname','doctors__name','submission_time')
	#每页显示条数
	list_per_page = 50

class PaymentAdmin(admin.ModelAdmin):
	list_display = ('id', 'visit_card','缴费项目')
	#可跳转字段
	list_display_links = ('id', 'visit_card','缴费项目')
	#可搜索字段
	search_fields =('visit_card__realname','缴费项目')
	#每页显示条数
	list_per_page = 50
	#多对多字段编辑
	filter_horizontal=('payment_item',)

	def 缴费项目(self,obj):
		return [item.name for item in  obj.payment_item.all()]

class PaymentItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','price')
	#可跳转字段
	list_display_links = ('id', 'name','price')
	#可搜索字段
	search_fields =('name',)
	#每页显示条数
	list_per_page = 50

class ReportAdmin(admin.ModelAdmin):
	list_display = ('id','visit_card', 'doctors','submission_time')
	#可跳转字段
	list_display_links = ('id','visit_card', 'doctors','submission_time')
	#可搜索字段
	search_fields =('visit_card__realname','doctors__name',)
	#过滤器字段
	list_filter =('submission_time',) 
	#每页显示条数
	list_per_page = 50


admin.site.register(DepartmentClassification, DepartmentClassificationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(RegisteredRecord, RegisteredRecordAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentItem, PaymentItemAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(DoctorVisitsNumber, DoctorVisitsNumberAdmin)