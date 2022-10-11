
from rest_framework import serializers
from User.serializer import UserSerializer

from transactions import models


class TypeSerializer(serializers.ModelSerializer):
    """Type serializer"""

    class Meta:
        """Meta class for type serializer"""

        model = models.Type
        fields = "__all__"


class TransactionDetailSerializer(serializers.ModelSerializer):
    """Transaction Detail serializer"""

    user = UserSerializer(read_only=True)

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


class ListTransactionSerializer(serializers.Serializer):
    '''List Transaction Serializer'''
    transactions = TransactionSerializer(many=True, read_only=True )
    subtotal = serializers.SerializerMethodField()


 
