# Generated by Django 4.1.2 on 2022-10-07 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CNABFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=30)),
                (
                    "nature",
                    models.CharField(
                        choices=[("Saída", "Outcome"), ("Entrada", "Income")],
                        max_length=30,
                    ),
                ),
                (
                    "signal",
                    models.CharField(
                        choices=[("+", "Plus"), ("-", "Minus")], max_length=1
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transaction_date", models.DateField()),
                ("transaction_time", models.TimeField()),
                ("amount", models.FloatField()),
                ("CPF", models.IntegerField()),
                ("card", models.IntegerField()),
                ("shop_rep", models.CharField(max_length=14)),
                ("shop_name", models.CharField(max_length=19)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="transactions.type",
                    ),
                ),
            ],
        ),
    ]
