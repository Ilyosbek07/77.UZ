from apps.common.models import StaticContent
from apps.store.models import Region
from rest_framework import generics
from rest_framework.views import APIView
from apps.common.serializers import RegionDistrictsSerializer, StaticContentSerializer
from rest_framework.response import Response


class RegionDistrictsAPIView(APIView):
    def get(self, request):
        query = Region.objects.all()
        serializer = RegionDistrictsSerializer(instance=query, many=True)
        return Response(serializer.data, status=200)


class StaticContentBySlugView(APIView):
    def get(self, request, slug):
        try:
            static_content = StaticContent.objects.get(slug=slug)
        except StaticContent.DoesNotExist:
            return Response({"detail": "Static content not found."}, status=404)
        serializer = StaticContentSerializer(static_content)
        return Response(serializer.data, status=200)
