from django.contrib import admin
from HospitalBusiness.models import DepartmentClassification,Department,Shift,RegisteredRecord

# Register your models here.
class DepartmentClassificationAdmin(admin.ModelAdmin):
	pass

class DepartmentAdmin(admin.ModelAdmin):
	# list_display = ('id', 'title', 'release_time','visits')

	# list_display_links = ('id', 'title')
	filter_horizontal=('doctors',)

class ShiftAdmin(admin.ModelAdmin):
	filter_horizontal=('doctor_duty',)

class RegisteredRecordAdmin(admin.ModelAdmin):
	pass

admin.site.register(DepartmentClassification, DepartmentClassificationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(RegisteredRecord, RegisteredRecordAdmin)