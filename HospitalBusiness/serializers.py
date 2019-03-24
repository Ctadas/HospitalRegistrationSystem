from rest_framework import serializers
from HospitalBusiness.models import Department,Shift,RegisteredRecord

class DoctorsField(serializers.CharField):
	def to_representation(self, value):
		# value就是每个QuerySet对象
		return {'id':value.id, "name": value.name, "job_title":value.job_title,"avatar":'http://localhost:8000'+value.avatar.url,'doctor_introduction':value.doctor_introduction}


class DepartmentSerializers(serializers.ModelSerializer):
	category = serializers.CharField(source="category.name")
	doctors = serializers.ListField(child=DoctorsField(),source="doctors.all")

	class Meta:
		model = Department
		fields = '__all__'

class ShiftSerializers(serializers.ModelSerializer):
	class Meta:
		model = Shift
		fields = '__all__'

class RegisteredRecordSerializers(serializers.ModelSerializer):
	visit_card_obj = serializers.ReadOnlyField()
	department = serializers.CharField(source="department.name")
	doctors_obj = serializers.ReadOnlyField()

	class Meta:
		model = RegisteredRecord
		fields = '__all__'