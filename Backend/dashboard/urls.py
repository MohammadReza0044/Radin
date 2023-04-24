from dashboard import views
from django.urls import include, path
from rest_framework import routers

app_name = "dashboard"

router = routers.SimpleRouter()
router.register("to-do", views.ToDoListSetView, basename="to-do")


urlpatterns = [
    path("", include(router.urls)),
]
