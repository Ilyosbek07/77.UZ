from django.urls import path
from apps.common.views import RegionDistrictsAPIView

urlpatterns = [
    path("regions-with-districts/", RegionDistrictsAPIView.as_view(), name="list_region_districts")
]
