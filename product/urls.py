from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('flowers', views.FlowersViewSet)
router.register('gifts', views.GiftsViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
