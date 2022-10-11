from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
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


class CreateListTransactionView(generics.ListCreateAPIView):
    """Create List Transaction view"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminOrOwner]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('shop_name')

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


class RetrieveUpdateDeleteTransactionView(generics.RetrieveUpdateDestroyAPIView):
    """Retruve Update Delete transaction view"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated | IsAdminOrOwner]

    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer
    lookup_url_kwarg = "transaction_id"


class CreateListTypeView(generics.ListCreateAPIView):
    """Create and list type view"""

    queryset = Type.objects.all()

    serializer_class = TypeSerializer
