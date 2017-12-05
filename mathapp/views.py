from django.shortcuts import render
from rest_framework import viewsets
from .models import CrossProduct
from .serializers import CrossProductSerializer
# Create your views here.

class CrossProductViewSet(viewsets.ModelViewSet):
	queryset = CrossProduct.objects.all()
	serializer_class = CrossProductSerializer
	http_method_names = ['get', 'post', 'head']