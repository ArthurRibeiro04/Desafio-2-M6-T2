# Generated by Django 4.1.5 on 2023-01-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Operation",
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
                ("Transaction_type", models.CharField(max_length=1)),
                ("Data", models.CharField(max_length=20)),
                ("Value", models.CharField(max_length=100)),
                ("CPF", models.CharField(max_length=100)),
                ("Card", models.CharField(max_length=100)),
                ("Time", models.CharField(max_length=100)),
                ("Owner", models.CharField(max_length=100)),
                ("Shop_name", models.CharField(max_length=100)),
            ],
        ),
    ]