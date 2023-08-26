from rest_framework import serializers
from apps.store.models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            "id",
            "name"
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
