from account.permissions import IsCEOOrIsAdministration
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import ManagerMessage, ToDoList
from .permissions import IsUser
from .serializers import ManagerMessageSerializer, ToDoListSerializer


class ToDoListSetView(ModelViewSet):
    serializer_class = ToDoListSerializer
    permission_classes = (IsAuthenticated, IsUser)

    def get_queryset(self):
        user = self.request.user
        return ToDoList.objects.filter(user=user)


class ManagerMessageSetView(ModelViewSet):
    queryset = ManagerMessage.objects.all()[:1]
    serializer_class = ManagerMessageSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsCEOOrIsAdministration]
        return [permission() for permission in permission_classes]
