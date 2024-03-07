from rest_framework.routers import DefaultRouter
from .viewsets import PessoaViewSet
from django.urls import include, path

router = DefaultRouter()

router.register(prefix="pessoa",viewset=PessoaViewSet)

urlpatterns = [
    path("api",include(router.urls))
]