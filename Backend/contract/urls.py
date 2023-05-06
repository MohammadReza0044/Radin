from contract import views
from django.urls import include, path
from rest_framework import routers

app_name = "contract"

router = routers.SimpleRouter()
router.register("contracts", views.ContractViewSet, basename="contract")


urlpatterns = [
    path("", include(router.urls)),
]
