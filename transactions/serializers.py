from rest_framework import serializers

from transactions import models


class TransactionDetailSerializer(serializers.ModelSerializer):
    """Transaction Detail serializer"""

    class Meta:
        """Meta Class of Transaction Detail Serializer"""

        model = models.Transaction
        fields = "__all__"
        depth = 1


class TransactionSerializer(serializers.ModelSerializer):
    """Transaction Serializer"""

    class Meta:
        """Meta Class for Transaction Serializer"""

        model = models.Transaction
        fields = "__all__"


class CNABFIleSerializer(serializers.ModelSerializer):
    """CNABFile  serializer"""

    class Meta:
        """Meta Class of CNABFile  Serializer"""

        model = models.CNABFile
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    """Type serializer"""

    class Meta:
        """Meta class for type serializer"""

        model = models.Type
        fields = "__all__"
