from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Vacation
from .permissions import IsCEOOrIsAdministration
from .serializers import ProfileSerializer, UserSerializer, VacationSerializer


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


class VacationViewSet(ModelViewSet):
    serializer_class = VacationSerializer
    search_fields = [
        "user__first_name",
        "user__last_name",
        "id",
    ]

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_Employee:
            return Vacation.objects.filter(user=user)
        else:
            return Vacation.objects.all()

    def get_permissions(self):
        if self.action in ["list", "create", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsCEOOrIsAdministration]
        return [permission() for permission in permission_classes]


class Profile(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return get_user_model().objects.get(pk=self.request.user.pk)
