from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import RobotCreateViewSet

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('robots', RobotCreateViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
