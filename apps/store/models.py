from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="category_icons/", blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="subcategories"
    )

    def __str__(self):
        return self.name


class Photo(BaseModel):
    image = models.ImageField(upload_to="ad_photos/")

    def __str__(self):
        return self.image.name


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return self.name


class Address(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    long = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return self.name


class Ad(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("moderation", "Moderation"),
        ("rejected", "Rejected"),
    )
    CURRENCY_CHOICES = (("uzs", "Uzbekistan Som"), ("usd", "US Dollar"))
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="ads"
    )
    photos = models.ManyToManyField(Photo)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="uzs")
    published_at = models.DateTimeField(auto_now_add=True)
    description = RichTextField()
    phone_number = models.CharField(max_length=20)
    address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name="ads")
    seller = models.ForeignKey(
        "users.Profile", on_delete=models.CASCADE, related_name="ads"
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{self.pk}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PopularSearch(models.Model):
    keyword = models.CharField(max_length=255, unique=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.keyword
