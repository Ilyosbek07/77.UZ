from rest_framework import serializers
from apps.store.models import Region, District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = (
            "id",
            "name"
        )


class RegionDistrictsSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True)

    class Meta:
        model = Region
        fields = (
            "id",
            "name",
            "districts"
        )
