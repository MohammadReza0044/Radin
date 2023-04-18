from account import views
from django.urls import include, path
from rest_framework import routers

app_name = "account"

router = routers.SimpleRouter()
router.register("users", views.UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
]
