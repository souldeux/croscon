from rest_framework import serializers
from .models import CrossProduct
import numpy

class CrossProductSerializer(serializers.HyperlinkedModelSerializer):

	#set a view_name explicitly here to avoid namespace issues
	url = serializers.HyperlinkedIdentityField(view_name = 'api:crossproduct-detail')

	def validate(self, data):
		"""
		Run some sanity checks on the vector values we receive
		"""
		#vectors must be comma-separated strings of integers
		try:
			v1_list = [int(x.strip()) for x in data['vector1'].split(',')]
			v2_list = [int(i.strip()) for i in data['vector2'].split(',')]
		except:
			raise serializers.ValidationError("Must provide only comma-separated integers")

		#vectors must be of equal length
		if not len(v1_list) == len(v2_list):
			raise serializers.ValidationError("Vectors to be multiplied must be of equal length")

		try:
			data['result'] = ','.join([str(x) for x in numpy.cross(v1_list, v2_list)])
		except Exception as e:
			#This could represent a data leak in an enterprise application, but 
			#for since this is a code challenge it makes sense to expose
			#the text of any error we hit here for transparency's sake
			raise serializers.ValidationError(e)

		return data


	class Meta:
		model = CrossProduct
		fields = (
			'vector1',
			'vector2',
			'result',
			'created',
			'url',
			)
		read_only_fields = ('result', 'created')