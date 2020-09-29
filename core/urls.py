from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'answer', views.AnswersView, 'answer'),
router.register(r'tag', views.TagsView, 'tag')
urlpatterns = [
    path('question/', views.QuestionsView.as_view(), name='question'),
    path('question/<int:question_id>/', views.QuestionDetailView.as_view(), name='question-detail')
]
urlpatterns.extend(router.urls)