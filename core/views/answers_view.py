from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Answer
from core.pagination import StandardResultsSetPagination
from core.serializers import AnswersSerializer


class AnswersView(viewsets.ViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswersSerializer
