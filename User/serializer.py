from rest_framework import serializers

from User.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    """User Detail serializer"""

    class Meta:
        """Meta Class of User Detail Serializer"""

        model = User
        fields = "__all__"
        depth = 1
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)

        return user


class UserSerializer(serializers.ModelSerializer):
    """User  serializer"""

    class Meta:
        """Meta Class of User  Serializer"""

        model = User
        exclude = ["is_active", "is_staff", "groups", "user_permissions"]
        read_only_fields = ["id", "date_joined", "is_superuser", "last_login"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
    
        user = User.objects.create_user(**validated_data)

        return user
