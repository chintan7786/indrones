# Generated by Django 4.1.3 on 2022-11-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Files",
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
                ("File_name", models.CharField(max_length=50)),
                ("File", models.FileField(upload_to="files")),
            ],
        ),
    ]
