from django.db import models #pragma: no cover
from django.urls import reverse #pragma: no cover

# Create your models here.
class CrossProduct(models.Model): #pragma: no cover
	"""
	Stores three values: two vectors of arbitrary and equal length, and their computed
	cross-product. Since there is no "ListField" or equivalent we choose to store vectors
	as strings of comma-separated values:
		"1,2,3,4"
	"""
	vector1 = models.CharField(max_length = 255)
	vector2 = models.CharField(max_length = 255)
	result = models.CharField(max_length = 255)
	created = models.DateTimeField(auto_now_add = True)

	def get_absolute_url(self): #pragma: no cover
		return reverse('api:crossproduct-detail', kwargs={'pk':self.pk})

	def __str__(self): #pragma: no cover
		return '{}'.format(self.id, self.created)

	class Meta: #pragma: no cover
		ordering = ('-created',)
		verbose_name_plural = 'CrossProducts'