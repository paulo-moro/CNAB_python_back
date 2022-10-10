from enum import unique
from django.conf import settings
from django.db import models

import os

# Create your models here.

from django.core.exceptions import ValidationError


class Transaction(models.Model):
    """Models for Transaction"""

    transaction_date = models.DateField()
    transaction_time = models.TimeField()
    amount = models.FloatField()
    CPF = models.IntegerField()
    card = models.CharField(max_length=12)
    shop_rep = models.CharField(max_length=14)
    shop_name = models.CharField(max_length=19)
    type = models.ForeignKey(
        "transactions.Type",
        on_delete=models.CASCADE,
        related_name="transactions",
    )


class NatureChoices(models.TextChoices):
    """Nature type Choices"""

    OUTCOME = "Saída"
    INCOME = "Entrada"


class SignalChoices(models.TextChoices):
    """Signal Choices"""

    PLUS = "+"
    MINUS = "-"


class Type(models.Model):
    """Type Models"""

    description = models.CharField(max_length=30)
    nature = models.CharField(max_length=30, choices=NatureChoices.choices)
    signal = models.CharField(max_length=1, choices=SignalChoices.choices)


MB = 2
MAX_SIZE = MB * 1024 * 1024


def validate_file_size(file):
    """Validation file size function, take a file as argument"""

    dir(file)
    if file.size > MAX_SIZE:
        raise ValidationError(f"File exceed maximum size {MB}mb")


class CNABFile(models.Model):
    """Model for CNAB file"""

    title = models.CharField(max_length=50, unique=True)
    file = models.FileField(validators=[validate_file_size])
