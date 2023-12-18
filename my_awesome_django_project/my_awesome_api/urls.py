from django.urls import include, path
from my_awesome_api.views import PersonViewSet, SpeciesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
