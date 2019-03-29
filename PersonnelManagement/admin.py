from django.contrib import admin
from PersonnelManagement.models import DoctorInformation,PatientInformation,VisitCard
# Register your models here.
class VisitCardAdmin(admin.ModelAdmin):
	#显示字段
	list_display = ('id', 'real_name', 'id_card','id_type','telphone')
	#可跳转字段
	list_display_links = ('id', 'real_name', 'id_card','id_type','telphone')
	#过滤器字段
	list_filter =('id_type',) 
	#可搜索字段
	search_fields =('real_name', 'id_card','id_type','telphone')
	#每页显示条数
	list_per_page = 50

class DoctorInformationAdmin(admin.ModelAdmin):
	#显示字段
	list_display = ('id', 'name', 'job_title')
	#可跳转字段
	list_display_links = ('id', 'name', 'job_title')
	#过滤器字段
	list_filter =('job_title',) 
	#可搜索字段
	search_fields =('name', 'job_title')
	#每页显示条数
	list_per_page = 50


class PatientInformationAdmin(admin.ModelAdmin):
	 # list_display = ('id', 'title', 'release_time','visits')

	 # list_display_links = ('id', 'title')
	 pass

admin.site.register(VisitCard, VisitCardAdmin)
admin.site.register(DoctorInformation, DoctorInformationAdmin)
admin.site.register(PatientInformation, PatientInformationAdmin)