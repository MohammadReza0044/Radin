from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsCEOOrIsAdministration
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsCEOOrIsAdministration)
    search_fields = [
        "first_name",
        "last_name",
        "personal_number",
        "phone_number",
    ]
