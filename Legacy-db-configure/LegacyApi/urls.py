from django.urls import path, include
from rest_framework import routers
from LegacyApi import views

router = routers.DefaultRouter()
router.register('legacy', views.LegacyTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
