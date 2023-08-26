from django.urls import path
from apps.store.views import (
    SearchPopularAPIView, AutoCompleteSearchView,
    CategoriesAPIView, AdCreateAPIView
)

urlpatterns = [
    path("search/populars/", SearchPopularAPIView.as_view(), name="popular_search"),
    path("search/complete/", AutoCompleteSearchView.as_view(), name="autocomplete_search"),
    path("categories-with-childs/", CategoriesAPIView.as_view(), name="categories"),
    path("store/ads/", AdCreateAPIView.as_view(), name="ad_create"),
]
