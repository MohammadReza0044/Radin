from account.models import User
from rest_framework import serializers

from .models import ManagerMessage, ToDoList, WorkingDay, WorkingMonth


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


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = "__all__"


class WorkingMonthSerializer(serializers.ModelSerializer):
    working_day = WorkingDaySerializer(many=True, read_only=True)
    days = serializers.ListField(
        child=serializers.DateField(),
        write_only=True,
    )

    class Meta:
        model = WorkingMonth
        fields = "__all__"

    def create(self, validated_data):
        days = validated_data.pop("days")
        month = WorkingMonth.objects.create(**validated_data)
        for day in days:
            new_month = WorkingDay.objects.create(month=month, working_day=day)
        return month

    def clear_existing_days(self, instance):
        old_days = WorkingDay.objects.filter(month_id=instance.id)

        for i in old_days:
            i.delete()

    def update(self, instance, validated_data):
        days = validated_data.pop("days", None)
        if days:
            self.clear_existing_days(instance)
            working_day_model_instance = [
                WorkingDay(month=instance, working_day=day) for day in days
            ]
            WorkingDay.objects.bulk_create(working_day_model_instance)
        return super().update(instance, validated_data)
