from apps.store.filters import AdFilter, ProfileAdsFilter
from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework import generics
from apps.store.models import PopularSearch, Ad, Category
from apps.store.serializers import CategoryListSerializer, AdSerializer


class SearchPopularAPIView(APIView):
    def get(self, request):
        popular = PopularSearch.objects.order_by("-count")[:10]
        popular_keywords = [item.keyword for item in popular]
        return Response(popular_keywords, status=200)


class AutoCompleteSearchView(APIView):
    def get(self, request):
        search_terms = Ad.objects.values_list(
            "keyword", flat=True
        )

        return Response(search_terms, status=200)


class CategoriesAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class AdCreateAPIView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filterset_class = AdFilter


class RetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = "slug"


class UserAdsListAPIView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filterset_class = ProfileAdsFilter
