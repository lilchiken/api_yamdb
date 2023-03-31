from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ReviewViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'titles/(?P<id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router.register(r'titles/\d+/reviews/(?P<id>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/', include(router.urls))
]
