# Create your views here.
from rest_framework import generics
from transactions.models import CNABFile, Type
from rest_framework import status
from rest_framework.response import Response

from transactions.serializers import (
    CNABFIleSerializer,
    TransactionSerializer,
    TypeSerializer,
)
from transactions.utils.handle_cnab import read_cnab, transaction_transcription

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

    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        stored_file = CNABFile.objects.get(id=kwargs["cnab_id"])
        path = f"uploads/{stored_file.file.name}"

        serializer = self.get_serializer
        file_data = read_cnab(path)

        response_list = transaction_transcription(
            file_data, self.perform_create, serializer
        )

        return Response(
            response_list,
            status=status.HTTP_201_CREATED,
        )


class CreateListTypeView(generics.ListCreateAPIView):
    """Create and list type view"""

    queryset = Type.objects.all()

    serializer_class = TypeSerializer
