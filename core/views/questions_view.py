from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from core.constants import open_status
from core.models import Question
from core.pagination import StandardResultsSetPagination
from core.serializers import QuestionSerializer, QuestionViewSerializer


class QuestionFilter(DjangoFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset


class QuestionsView(APIView):
    filter_fields = ('tags', 'tags__code', 'tags__name')

    def get(self, request):
        question = Question.objects.filter(status=open_status)
        question_filter = QuestionFilter()
        filtered_queryset = question_filter.filter_queryset(request, question, self)
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(filtered_queryset, request)
        serializer = QuestionViewSerializer(result_page, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, question_id):
        try:
            return Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, question_id):
        question = self.get_object(question_id)
        serializer = QuestionViewSerializer(question)
        return Response(serializer.data)

    def put(self, request, question_id):
        question = self.get_object(question_id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, question_id):
        question = self.get_object(question_id)
        vote = request.data.get('vote')
        if vote is not None and isinstance(vote, int):
            request.data['vote'] = vote + question.vote
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        question = self.get_object(question_id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
