from rest_framework import serializers
from PersonnelManagement.models import VisitCard

class VisitCardSerializers(serializers.ModelSerializer):
	class Meta:
		model = VisitCard
		fields = '__all__'