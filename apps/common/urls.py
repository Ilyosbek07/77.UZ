from django.urls import path
from apps.common.views import RegionDistrictsAPIView, StaticContentBySlugView

urlpatterns = [
    path("regions-with-districts/", RegionDistrictsAPIView.as_view(), name="list_region_districts"),
    path("pages/<slug:slug>/", StaticContentBySlugView.as_view(), name="static-content-by-slug")
]
