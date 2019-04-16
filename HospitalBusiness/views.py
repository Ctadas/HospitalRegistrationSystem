from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from HospitalBusiness.models import Department,Shift,RegisteredRecord,Payment,Report,DoctorVisitsNumber
from HospitalBusiness.serializers import DepartmentSerializers,ShiftSerializers,RegisteredRecordSerializers,PaymentSerializers,ReportSerializers
from PersonnelManagement.models import DoctorInformation,PatientInformation,VisitCard
from django.http import HttpResponse
import json
# Create your views here.

#获取医院部门信息
@api_view(['GET'])
def get_department_info(request):
	departmen = Department.objects.all()
	if request.method == 'GET':
		serializer = DepartmentSerializers(departmen, many=True)
		return Response(serializer.data)

#获取值班信息
@api_view(['GET'])
def get_shift(request):
	visit_date = request.GET.get('visit_date')
	shift = Shift.objects.filter(time = visit_date)
	if request.method == 'GET':
		serializer = ShiftSerializers(shift, many=True)
		return Response(serializer.data)

#新增挂号记录
@api_view(['POST'])
def commit_registered_record(request):
	if request.method == 'POST':
		data = json.loads(request.body.decode())
		department_name = data['department_name']
		date = data['date']
		visitcard_id = data['visitcard_id']
		doctor_id = data['doctor_id']
		openid = data['openid']

		department = Department.objects.get(name = department_name)
		registered_date = date
		visit_card = VisitCard.objects.get(id = visitcard_id)
		doctors = DoctorInformation.objects.get(id = doctor_id)
		wx_id = PatientInformation.objects.get(openid = openid)
		r = RegisteredRecord.objects.create(
			department = department, 
			registered_date= registered_date,
			visit_card=visit_card,
			doctors= doctors
			)
		visit_number = DoctorVisitsNumber.objects.get(doctor = doctors,visit_time = registered_date)
		visit_number.visit_number = visit_number.visit_number - 1
		visit_number.association_registered_record.add(r)
		visit_number.save()

		return Response(1)

#获取挂号记录
@api_view(['GET'])
def get_registered_record(request):
	visit_cardid = request.GET.get('visit_cardid')

	visit_card_obj = VisitCard.objects.get(id = visit_cardid)

	registered_record = RegisteredRecord.objects.filter(visit_card = visit_card_obj).order_by('-submission_time')

	if request.method == 'GET':
		serializer = RegisteredRecordSerializers(registered_record, many=True)
		return Response(serializer.data)

#获取缴费内容
@api_view(['GET'])
def get_payment(request):
	visit_cardid = request.GET.get('visit_cardid')

	visit_card_obj = VisitCard.objects.get(id = visit_cardid)

	payment = Payment.objects.filter(visit_card = visit_card_obj)

	if request.method == 'GET':
		serializer = PaymentSerializers(payment, many=True)
		return Response(serializer.data)

#获取就诊报告
@api_view(['GET'])
def get_report(request):
	visit_cardid = request.GET.get('visit_cardid')

	visit_card_obj = VisitCard.objects.get(id = visit_cardid)

	report = Report.objects.filter(visit_card = visit_card_obj).order_by('-submission_time')

	if request.method == 'GET':
		serializer = ReportSerializers(report, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def get_doctor_visits_number(request):
	id_list = request.GET.get('id_list')
	visit_time = request.GET.get('visit_time')
	id_list = json.loads(id_list)
	visit_number = {}

	for doctor_id in id_list:
		doctor = DoctorInformation.objects.get(id = doctor_id)
		doctor_visits_number = DoctorVisitsNumber.objects.get(doctor = doctor,visit_time = visit_time)
		visit_number[doctor_visits_number.doctor.id] = doctor_visits_number.visit_number
	return Response(visit_number)
