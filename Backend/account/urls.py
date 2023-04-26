from account import views
from django.urls import include, path
from rest_framework import routers

app_name = "account"

router = routers.SimpleRouter()
router.register("users", views.UserViewSet, basename="users")
router.register("vacations", views.VacationViewSet, basename="vacations")


urlpatterns = [
    path("", include(router.urls)),
    path("profile/", views.Profile.as_view(), name="profile"),
]
