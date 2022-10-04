from django.db import models

# Create your models here.


class Transaction(models.Model):
    """Models for Transaction"""

    transaction_date = models.DateField()
    transaction_time = models.TimeField()
    amount = models.FloatField()
    CPF = models.IntegerField()
    card = models.IntegerField()
    shop_rep = models.CharField(max_length=14)
    shop_name = models.CharField(max_length=19)


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
    transaction = models.ForeignKey(
        "transactions.Transaction",
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    transaction = models.OneToOneField(
        "transactions.Transaction", on_delete=models.CASCADE
    )
