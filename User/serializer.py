from rest_framework import serializers

from User.models import User
from transactions.serializers import TransactionDetailSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    """User Detail serializer"""

    transactions = TransactionDetailSerializer(many=True)

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
        fields = "__all__"
