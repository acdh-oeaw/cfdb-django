# Generated by Django 5.0.6 on 2024-06-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("labels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Normalisierte, gegenwärtige Ortsbezeichnung",
                        max_length=250,
                    ),
                ),
                (
                    "geonames_id",
                    models.CharField(blank=True, help_text="GND-ID", max_length=50),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True, decimal_places=12, max_digits=20, null=True
                    ),
                ),
                (
                    "lng",
                    models.DecimalField(
                        blank=True, decimal_places=12, max_digits=20, null=True
                    ),
                ),
                (
                    "alternative_name",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Alternative names",
                        max_length=250,
                        to="labels.label",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]
