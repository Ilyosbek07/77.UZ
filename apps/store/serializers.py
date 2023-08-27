from apps.users.models import User
from rest_framework import serializers
from apps.store.models import (
    Category,
    SubCategory,
    Ad,
    Photo,
    Address,
    Region,
    District,
)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("image",)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name")


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = District
        fields = ("id", "name", "region")


class AddressSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()
    lat = serializers.IntegerField()
    long = serializers.IntegerField()

    class Meta:
        model = Address
        fields = ("district", "name", "lat", "long")


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("id", "name")


class CategoryListSerializer(serializers.ModelSerializer):
    ads_count = serializers.SerializerMethodField()
    subcategories = SubCategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "ads_count", "icon", "subcategories")

    def get_ads_count(self, obj):
        total_ads_count = 0
        for subcategory in obj.subcategories.all():
            total_ads_count += subcategory.ads.count()
        return total_ads_count


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = SubCategory
        fields = ("id", "name", "category")


class AdUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
        )


class AdSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer()
    photos = PhotoSerializer(many=True)
    address = AddressSerializer()
    seller = AdUserSerializer()
    price = serializers.IntegerField()

    class Meta:
        model = Ad
        fields = (
            "id",
            "name",
            "slug",
            "sub_category",
            "photos",
            "price",
            "currency",
            "published_at",
            "description",
            "phone_number",
            "address",
            "seller",
            "status",
            "expires_at",
        )
