from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


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
