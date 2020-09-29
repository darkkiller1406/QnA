from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Answer, Question, Tag


class AnswerSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        if self.partial:
            vote = validated_data.get('vote')
            if vote is not None:
                validated_data['vote'] = vote + instance.vote
        response = super(AnswerSerializer, self).update(instance, validated_data)
        return response

    class Meta:
        model = Answer
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionViewSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
