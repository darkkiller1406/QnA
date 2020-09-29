from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from core.pagination import StandardResultsSetPagination
from core.serializers import TagSerializer


class TagsView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer
