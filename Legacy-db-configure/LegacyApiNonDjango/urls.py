from django.urls import path, include
from rest_framework import routers
from LegacyApiNonDjango import views

router = routers.DefaultRouter()
router.register('legacy', views.LegacyActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
