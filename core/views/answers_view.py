from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Answer, Question
from core.pagination import StandardResultsSetPagination
from core.serializers import AnswersSerializer, QuestionSerializer


class AnswersView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswersSerializer


class QuestionsView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
