from rest_framework.routers import DefaultRouter

from django.urls import (include, path)

from api.views import (TitlesViewSet, CategoriesViewSet, GenresViewSet)

router_v1 = DefaultRouter()
router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register('genres', GenresViewSet, basename='genres')
router_v1.register('categories', CategoriesViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
