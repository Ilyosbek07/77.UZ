from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework import generics
from apps.store.models import PopularSearch, Ad, Category
from apps.store.serializers import CategoryListSerializer


class SearchPopularAPIView(APIView):
    def get(self, request):
        popular = PopularSearch.objects.order_by('-count')[:10]
        popular_keywords = [item.keyword for item in popular]
        return Response(popular_keywords, status=200)


class AutoCompleteSearchView(APIView):
    def get(self, request):
        search_terms = Ad.objects.values_list('keyword', flat=True)  # Fetch search terms from the model

        return Response(search_terms, status=200)


class CategoriesAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
