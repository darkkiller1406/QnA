from rest_framework import viewsets

from core.models import Tag
from core.pagination import StandardResultsSetPagination
from core.serializers import TagSerializer


class TagsView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
