from django.urls import path
from apps.store.views import SearchPopularAPIView

urlpatterns = [
    path("search/populars", SearchPopularAPIView.as_view(), name="popular_search")
]
