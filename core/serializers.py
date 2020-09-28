from rest_framework.serializers import ModelSerializer

from core.models import Answer


class AnswersSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

