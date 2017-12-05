from django.db import models
from django.urls import reverse

# Create your models here.
class CrossProduct(models.Model):
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

	def get_absolute_url(self):
		return reverse('api:crossproduct-detail', kwargs={'pk':self.pk})

	def __str__(self):
		return '{}'.format(self.id, self.created)

	class Meta:
		ordering = ('-created',)
		verbose_name_plural = 'CrossProducts'