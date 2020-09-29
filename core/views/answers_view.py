from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Answer
from core.pagination import StandardResultsSetPagination
from core.serializers import AnswerSerializer


class AnswersView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
