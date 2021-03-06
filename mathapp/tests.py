from rest_framework.test import APITestCase, APIClient
from django.db.models import CharField, DateTimeField
import unittest, numpy, json
from .models import CrossProduct
from django.urls import reverse
from django.apps import apps
from django.test import TestCase
from .apps import MathappConfig

class TestCrossProductListCreateAPI(unittest.TestCase):
	url = reverse("api:crossproduct-list")
	def setUp(self):
		self.client = APIClient()
		self.vector1 = '1,2,3'
		self.vector2 = '4,5,6'

	def test_create_crossproduct(self):
		#Does the create API endpoint return a valid status code for valid data?
		#Does it save data properly?
		response = self.client.post(self.url, {
				'vector1': self.vector1,
				'vector2': self.vector2,
			})
		self.assertEqual(201, response.status_code)
		self.assertEqual(self.vector1, response.json()['vector1'])
		self.assertEqual(self.vector2, response.json()['vector2'])

	def test_valid_crossproduct_result(self):
		#Does the create API create objects with mathematically correct results?
		response = self.client.post(self.url, {
				'vector1': self.vector1,
				'vector2': self.vector2,
			})
		cp_control = numpy.cross(
				[int(i) for i in self.vector1.split(',')],
				[int(x) for x in self.vector2.split(',')]
			)
		result = response.json()['result']
		self.assertEqual( ','.join([str(c) for c in cp_control]), result )

	def test_crossproduct_list(self):
		#Does the list API list all objects?
		response = self.client.get(self.url)
		self.assertEqual( len(response.json()['results']),  CrossProduct.objects.count() )

	def test_bad_vectors(self):
		#Does the API return 400 responses for invalid vectors?
		
		#test unequal lengths
		bad_vector1 = '1,2,3'
		bad_vector2 = '4,5,6,7'
		response1 = self.client.post(self.url, {
				'vector1': bad_vector1,
				'vector2': bad_vector2
			})
		self.assertEqual( 400, response1.status_code )

		#test NaN values
		bad_vector3 = '1,2,!'
		response2 = self.client.post(self.url, {
				'vector1': bad_vector1,
				'vector2': bad_vector3
			})
		self.assertEqual( 400, response2.status_code )

		#test oversized inputs
		big_vector1 = ['1,'*200 + '1']
		big_vector2 = ['1,'*200 + '1']
		response3 = self.client.post(self.url, {
				'vector1': big_vector1,
				'vector2': big_vector2
			})
		self.assertEqual( 400, response3.status_code )

	def test_absolute_url(self):
		#Can we pull data properly from an object's absolute url?
		cp = CrossProduct.objects.create(vector1=self.vector1, vector2=self.vector2)
		response = self.client.get(cp.get_absolute_url())
		self.assertEqual(cp.vector1, response.json()['vector1'])
		self.assertEqual(cp.vector2, response.json()['vector2'])
		self.assertEqual(cp.result, response.json()['result'])

	def test_verbose_plural(self):
		#Does the verbose plural method work?
		self.assertEqual( str(CrossProduct._meta.verbose_name_plural), 'CrossProducts' )

	def test_apps_file(self):
		#is the apps.py file configured right?
		self.assertEqual(MathappConfig.name, 'mathapp')
		self.assertEqual(apps.get_app_config('mathapp').name, 'mathapp')

	def test_health_endpoint(self):
		response = self.client.get( reverse('api:health-list') )
		self.assertEqual(200, response.status_code)

