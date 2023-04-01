from django.urls import (
    path,
    include
)
from rest_framework.routers import DefaultRouter

from api.views import (TitleViewSet, CategorieViewSet,
                        GenreViewSet, ReviewViewSet, CommentViewSet)

router_v1 = DefaultRouter()
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('categories', CategorieViewSet, basename='categories')
router_v1.register(r'titles/(?P<id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router_v1.register(r'titles/\d+/reviews/(?P<id>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]