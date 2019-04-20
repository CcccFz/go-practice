from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import TodoViewSet


router = DefaultRouter()
router.register('', TodoViewSet)


urlpatterns = [
    url('', include(router.urls), name='todos'),
]
