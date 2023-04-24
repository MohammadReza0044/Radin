from account import views
from django.urls import include, path
from rest_framework import routers

app_name = "contract"

router = routers.SimpleRouter()


urlpatterns = [
    path("", include(router.urls)),
]
