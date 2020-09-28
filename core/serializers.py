from rest_framework.serializers import ModelSerializer

from core.models import Answer, Question


class AnswersSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(ModelSerializer):

    def update(self, instance, validated_data):
        vote = validated_data.get('vote')
        if vote is not None:
            validated_data['vote'] = vote + instance.vote
        response = super(QuestionSerializer, self).update(instance, validated_data)
        return response

    class Meta:
        model = Question
        fields = '__all__'
