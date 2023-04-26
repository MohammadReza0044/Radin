from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Vacation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = (
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
            "is_superuser",
            "is_staff",
            "is_active",
        )

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(UserSerializer, self).create(validated_data)


class VacationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )

    class Meta:
        model = Vacation
        fields = "__all__"
        extra_kwargs = {
            "from_hour": {"required": False},
            "untill_hour": {"required": False},
        }

    def validate(self, data):
        data_dict = dict(data)
        vacation_type = data_dict.get("vacation_type")
        if vacation_type == "Hourly" and data_dict.get("from_hour") == None:
            raise serializers.ValidationError(
                {"from_hour": ["ساعت شروع مرخصی باید وارد شود"]}
            )
        if vacation_type == "Hourly" and data_dict.get("untill_hour") == None:
            raise serializers.ValidationError(
                {"untill_hour": ["ساعت پایان مرخصی باید وارد شود"]}
            )
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "picture",
            "personal_number",
            "first_name",
            "last_name",
            "job_position",
            "job_description",
        )
