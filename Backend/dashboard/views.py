from rest_framework.viewsets import ModelViewSet

from .models import ToDoList
from .serializers import ToDoListSerializer


class ToDoListSetView(ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
