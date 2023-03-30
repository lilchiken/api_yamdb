from rest_framework import (viewsets, filters, permissions)
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import (Genre, Title, Category)

from api.serializers import (GenreSerializer, CategorySerializer,
                             TitleGetSerializer, TitlePostSerializer)



class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    lookup_value_regex = '[0-9a-f]{32}'


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)
    lookup_field = 'slug'
    lookup_value_regex = '[0-9a-f]{32}'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          permissions.IsAdminUser,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'category',
        'genre',
        'name',
        'year',
    )
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitleGetSerializer
        return TitlePostSerializer
