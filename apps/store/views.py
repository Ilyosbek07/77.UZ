from rest_framework.views import Response
from rest_framework.views import APIView
from apps.store.models import PopularSearch


class SearchPopularAPIView(APIView):
    def get(self, request):
        popular = PopularSearch.objects.order_by('-count')[:10]
        popular_keywords = [item.keyword for item in popular]
        return Response(popular_keywords, status=200)
