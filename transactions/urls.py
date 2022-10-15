from django.urls import path
from . import views


urlpatterns = [
    path("transactions/upload/", views.CreateUploadTransaction.as_view()),
    path("transactions/files/", views.ListUploads.as_view()),
    path("transactions/file/<cnab_id>/", views.RetrieveDeleteCNABFile.as_view()),
    path("transactions/type/", views.CreateListTypeView.as_view()),
    path("transaction/file/<cnab_id>/", views.CreateListTransactionView.as_view()),
    path("transactions/", views.CreateListTransactionView.as_view()),
   
    path(
        "transaction/<transaction_id>/",
        views.RetrieveUpdateDeleteTransactionView.as_view(),
    ),
]
