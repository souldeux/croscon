from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CrossProduct
from .serializers import CrossProductSerializer


class CrossProductViewSet(viewsets.ModelViewSet):
	queryset = CrossProduct.objects.all()
	serializer_class = CrossProductSerializer
	http_method_names = ['get', 'post', 'head']
	

class HealthViewSet(viewsets.GenericViewSet):
	def list(self, request, format=None):
		return Response({'message':'ok'}, status=status.HTTP_200_OK)