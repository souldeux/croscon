from django.conf.urls import url, include
from mathapp import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

router = DefaultRouter()
#registering like this means we lose the API root view and start directly with list view
router.register(r'compute', views.CrossProductViewSet)
router.register(r'health', views.Health, 'health')

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^api/', include(router.urls, namespace='api')),
]