from contract import views
from django.urls import include, path
from rest_framework import routers

app_name = "contract"

router = routers.SimpleRouter()
router.register("contract-type", views.ContractTypeViewSet, basename="contract-type")
router.register("receipt", views.ReceiptViewSet, basename="receipt")
router.register("contract", views.ContractViewSet, basename="contract")


urlpatterns = [
    path("", include(router.urls)),
]
