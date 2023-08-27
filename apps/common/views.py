from apps.store.models import Region
from rest_framework import generics
from rest_framework.views import APIView
from apps.common.serializers import RegionDistrictsSerializer
from rest_framework.response import Response


class RegionDistrictsAPIView(APIView):
    def get(self, request):
        query = Region.objects.all()
        serializer = RegionDistrictsSerializer(instance=query, many=True)
        return Response(serializer.data, status=200)


