from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134437ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134437", Testconnectors134437ViewSet, basename="testconnectors134437"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
