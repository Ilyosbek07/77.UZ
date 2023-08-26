import django_filters
from .models import Ad


class AdFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    region_id = django_filters.CharFilter(
        field_name="address__region__id", lookup_expr="contains"
    )
    district_id = django_filters.CharFilter(
        field_name="address__district__region__id", lookup_expr="contains"
    )
    category_ids = django_filters.CharFilter(method='filter_category_ids')
    sub_category_ids = django_filters.CharFilter(method='filter_sub_category_ids')
    price_gte = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    seller_id = django_filters.CharFilter(field_name="seller__id")

    class Meta:
        model = Ad
        fields = ("name", "sub_category", "address", "price")

    def filter_category_ids(self, queryset, name, value):
        ids_list = value.split(',')
        return queryset.filter(sub_category__category__id__in=ids_list)

    def filter_sub_category_ids(self, queryset, name, value):
        ids_list = value.split(',')
        return queryset.filter(sub_category__id__in=ids_list)


class ProfileAdsFilter(django_filters.FilterSet):

    class Meta:
        model = Ad

    def qs(self):
        queryset = super().qs
        user = self.request.user.id
        if user.is_authenticated:
            return queryset.filter(seller=user)
        return queryset.none()