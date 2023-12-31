# Generated by Django 4.2.3 on 2023-07-31 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Expense",
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
                (
                    "name",
                    models.CharField(max_length=140, verbose_name="Name of Expense"),
                ),
                ("date_of_expense", models.DateField(verbose_name="Date of Expense")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Health", "Health"),
                            ("Electronics", "Electronics"),
                            ("Travel", "Travel"),
                            ("Education", "Education"),
                            ("Books", "Books"),
                            ("Others", "Others"),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "amount",
                    models.PositiveIntegerField(default=0, verbose_name="Amount"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expenses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
