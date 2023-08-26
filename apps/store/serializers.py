from apps.users.models import User
from rest_framework import serializers
from apps.store.models import Category, SubCategory, Ad, Photo, Address


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            "id",
            "name"
        )


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "id",
            "image"
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "district",
            "name",
            "lat",
            "long"
        )


class CategoryListSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    total_ads_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "total_ads_count",
            "icon",
            "subcategories",
        )

    def get_total_ads_count(self, obj):
        total_ads_count = 0
        for subcategory in obj.subcategories.all():
            total_ads_count += subcategory.ads.count()
        return total_ads_count


class AdSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer()
    photos = PhotoSerializer(many=True)
    address = AddressSerializer()
    seller = UserSerializer()

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
            "expires_at"
        )
