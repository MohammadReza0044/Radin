from rest_framework import serializers

from .models import ToDoList, User


class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), queryset=User.objects.all()
    )

    class Meta:
        model = ToDoList
        fields = "__all__"
