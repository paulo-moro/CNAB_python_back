# Create your views here.
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from datetime import date, time, datetime
from User.permissions import IsAdminOrOwner
from transactions.models import CNABFile, Transaction, Type
from transactions.serializers import (
    CNABFIleSerializer,
    TransactionDetailSerializer,
    TransactionSerializer,
    TypeSerializer,
)
from transactions.utils.handle_cnab import (
    delete_cnab,
    read_cnab,
    transaction_transcription,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

# from transactions.models import Transaction


class CreateUploadTransaction(generics.CreateAPIView):
    """Create Transaction from a CNABFile"""

    serializer_class = CNABFIleSerializer


class ListUploads(generics.ListAPIView):
    """List uploaded CNAB Files"""

    queryset = CNABFile.objects.all()
    serializer_class = CNABFIleSerializer


class RetrieveDeleteCNABFile(generics.RetrieveDestroyAPIView):
    """View for deletion of uploaded file"""

    queryset = CNABFile.objects.all()
    lookup_url_kwarg = "cnab_id"


class CreateTransactionView(generics.CreateAPIView):
    """Create Transaction view"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminOrOwner]
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):

        cnab_id = kwargs["cnab_id"]
        stored_file = get_object_or_404(CNABFile, id=cnab_id)
        path = f"uploads/{stored_file.file.name}"

        serializer = self.get_serializer
        file_data = read_cnab(path)

        response_list = transaction_transcription(
            file_data, serializer, self.request.user
        )
        delete_cnab(path, cnab_id)

        return Response(
            response_list,
            status=status.HTTP_201_CREATED,
        )


class ListTransactionView(generics.ListAPIView):
    queryset = Transaction.objects.all()

    serializer_class = TransactionSerializer


class RetrieveUpdateDeleteTransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer
    lookup_url_kwarg = "transaction_id"


class CreateListTypeView(generics.ListCreateAPIView):
    """Create and list type view"""

    queryset = Type.objects.all()

    serializer_class = TypeSerializer
