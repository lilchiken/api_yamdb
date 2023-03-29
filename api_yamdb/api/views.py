from rest_framework import (
    viewsets,
    mixins,
    status,
    permissions
)
from rest_framework.response import Response

from api.serializers import AuthSerializer
from reviews.models import User


class AuthViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(instance, status.HTTP_200_OK)
