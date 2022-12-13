from django.urls import include, path
from rest_framework import routers
from MyAPI.api import HeroViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'heroes', HeroViewSet)

urlpatterns = [
    path('', include(router.urls))
]
