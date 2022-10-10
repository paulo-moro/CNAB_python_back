from django.urls import path
from . import views


urlpatterns = [
    path("transactions/upload/", views.CreateUploadTransaction.as_view()),
    path("transactions/files/", views.ListUploads.as_view()),
    path("transactions/file/<cnab_id>/", views.RetrieveDeleteCNABFile.as_view()),
    path("transactions/type/", views.CreateListTypeView.as_view()),
    path("transaction/<cnab_id>/", views.CreateTransactionView.as_view()),
]
