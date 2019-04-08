from django.shortcuts import render
from django.http import HttpResponse
from PersonnelManagement.models import PatientInformation,VisitCard
import requests as httprequests
import json 

from django.shortcuts import render
from PersonnelManagement.serializers import VisitCardSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# Create your views here.

#获取微信小程序的授权
def getLoginCode(request):

	url ='https://api.weixin.qq.com/sns/jscode2session'
	code = request.GET.get('code')
	appid = ''
	secret = ''
	params = {
		'appid':appid,
		'secret':secret,
		'js_code':code,
		'grant_type':'authorization_code'
	}
	return_request = httprequests.get(url,params)

	openid = return_request.json()['openid']
	session_key = return_request.json()['session_key']

	p  = PatientInformation.objects.filter(openid = openid)

	if p.exists():
		p  = PatientInformation.objects.get(openid = openid)
		p.session_key = session_key
		p.save()
	else:
		p  = PatientInformation.objects.create(openid = openid,session_key = session_key)

	print(return_request.json()['openid'])

	return_dict = {}
	return_dict['data'] = return_request.json()['openid']
	return HttpResponse(json.dumps(return_dict))

#新增就诊卡
@api_view(['POST'])
def add_VisitCard(request):
	data = request.data
	user_openid = data['user_openid']
	visit_card = data['visit_card']
	patien = PatientInformation.objects.get(openid = user_openid)

	if VisitCard.objects.filter(id_card=visit_card['id_card'],id_type=visit_card['id_type']):
		visit_card_object  = VisitCard.objects.get(
					id_card = visit_card['id_card'],
					id_type = visit_card['id_type']
					)
		patien.visit_card.add(visit_card_object)
		patien.save()
		return Response(json.dumps({}),status=status.HTTP_201_CREATED)
	else:
		if request.method == 'POST':
			serializer = VisitCardSerializers(data=visit_card)
			if serializer.is_valid():
				serializer.save()
				visit_card_object  = VisitCard.objects.get(
						id_card=serializer.data['id_card'],
						id_type = serializer.data['id_type'],
						)
				patien.visit_card.add(visit_card_object)
				patien.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#获取微信用户关联的就诊卡
@api_view(['GET'])
def get_VisitCard(request):
	openid = request.GET.get('openid')
	Patient = PatientInformation.objects.get(openid = openid)
	visit_card_object = Patient.visit_card.all()
	if request.method == 'GET':
		serializer = VisitCardSerializers(visit_card_object, many=True)
		return Response(serializer.data)

#获取就诊卡的详细信息
@api_view(['GET'])
def get_VisitCard_info(request):
	card_id = request.GET.get('id')
	visit_card_object = VisitCard.objects.get(id = card_id)
	if request.method == 'GET':
		serializer = VisitCardSerializers(visit_card_object)
		return Response(serializer.data)

#移除就诊卡关联
def remove_VisitCard(request):
	if request.method == 'GET':
		card_id = request.GET.get('card_id')
		openid = request.GET.get('openid')
		visit_card_object = VisitCard.objects.get(id = card_id)
		patien = PatientInformation.objects.get(openid = openid)
		patien.visit_card.remove(visit_card_object)
		patien.save()
		return HttpResponse('1')
	


