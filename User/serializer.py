from rest_framework import serializers

from User.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    """User Detail serializer"""

    class Meta:
        """Meta Class of User Detail Serializer"""

        model = User
        fields = "__all__"
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    """User  serializer"""

    class Meta:
        """Meta Class of User  Serializer"""

        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_superuser",
            "is_active",
            "date_joined",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)

        return user
