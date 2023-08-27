# Generated by Django 4.2.4 on 2023-08-26 11:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "icon",
                    models.ImageField(
                        blank=True, null=True, upload_to="category_icons/"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="ad_photos/")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PopularSearch",
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
                ("keyword", models.CharField(max_length=255, unique=True)),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategories",
                        to="store.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="District",
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
                ("name", models.CharField(max_length=100)),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.region"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("name", models.CharField(max_length=255)),
                ("lat", models.DecimalField(decimal_places=6, max_digits=10)),
                ("long", models.DecimalField(decimal_places=6, max_digits=10)),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.district"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ad",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "currency",
                    models.CharField(
                        choices=[("uzs", "Uzbekistan Som"), ("usd", "US Dollar")],
                        default="uzs",
                        max_length=3,
                    ),
                ),
                ("published_at", models.DateTimeField(auto_now_add=True)),
                ("description", ckeditor.fields.RichTextField()),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("moderation", "Moderation"),
                            ("rejected", "Rejected"),
                        ],
                        max_length=15,
                    ),
                ),
                ("expires_at", models.DateTimeField()),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ads",
                        to="store.address",
                    ),
                ),
                ("photos", models.ManyToManyField(to="store.photo")),
            ],
        ),
    ]
