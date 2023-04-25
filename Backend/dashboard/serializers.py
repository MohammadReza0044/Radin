from account.models import User
from rest_framework import serializers

from .models import ManagerMessage, ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), queryset=User.objects.all()
    )

    class Meta:
        model = ToDoList
        fields = "__all__"
        read_only_fields = ("user",)


class ManagerMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerMessage
        fields = "__all__"
