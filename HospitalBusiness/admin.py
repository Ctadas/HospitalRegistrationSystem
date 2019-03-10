from django.contrib import admin
from HospitalBusiness.models import DepartmentClassification,Department

# Register your models here.
class DepartmentClassificationAdmin(admin.ModelAdmin):
	pass

class DepartmentAdmin(admin.ModelAdmin):
	# list_display = ('id', 'title', 'release_time','visits')

	# list_display_links = ('id', 'title')
	filter_horizontal=('doctors',)

admin.site.register(DepartmentClassification, DepartmentClassificationAdmin)
admin.site.register(Department, DepartmentAdmin)