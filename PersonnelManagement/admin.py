from django.contrib import admin
from PersonnelManagement.models import DoctorInformation,PatientInformation,VisitCard
# Register your models here.
class VisitCardAdmin(admin.ModelAdmin):
	pass

class DoctorInformationAdmin(admin.ModelAdmin):
	pass

class PatientInformationAdmin(admin.ModelAdmin):
	 # list_display = ('id', 'title', 'release_time','visits')

	 # list_display_links = ('id', 'title')
	 pass

admin.site.register(VisitCard, VisitCardAdmin)
admin.site.register(DoctorInformation, DoctorInformationAdmin)
admin.site.register(PatientInformation, PatientInformationAdmin)