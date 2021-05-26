from django.urls import path, include
from rest_framework import routers
from Task import views

router = routers.DefaultRouter()
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
