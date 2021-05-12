from django.conf.urls import include
from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import Parliament1Viewset
from .views import Parliament1Viewsetpp
from .views import SearchAPIView

router = DefaultRouter()
router.register("list", Parliament1Viewset, basename="list")
router.register("list2", Parliament1Viewsetpp, basename="list2")


urlpatterns = [url("", include(router.urls)), path("search/", SearchAPIView.as_view())]
