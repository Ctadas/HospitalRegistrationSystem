from rest_framework import serializers
from HospitalBusiness.models import Department,Shift,RegisteredRecord,Payment,Report

class DoctorsField(serializers.CharField):
	def to_representation(self, value):
		# value就是每个QuerySet对象
		return {'id':value.id, "name": value.name, "job_title":value.job_title,"avatar":'http://localhost:8000'+value.avatar.url,'doctor_introduction':value.doctor_introduction}

class PaymentItemField(serializers.CharField):
	def to_representation(self, value):
		# value就是每个QuerySet对象
		return {'id':value.id, "name": value.name, "price":value.price}


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

class PaymentSerializers(serializers.ModelSerializer):
	visit_card_obj = serializers.ReadOnlyField()
	payment_item = serializers.ListField(child=PaymentItemField(),source="payment_item.all")

	class Meta:
		model = Payment
		fields = '__all__'

class ReportSerializers(serializers.ModelSerializer):
	visit_card_obj = serializers.ReadOnlyField()
	doctors_obj = serializers.ReadOnlyField()

	class Meta:
		model =  Report
		fields = '__all__'