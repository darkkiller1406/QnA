# from django.conf.urls import url
from django.urls import path
# from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'answer', views.AnswersView)
router.register(r'question', views.QuestionsView)
urlpatterns = [
    # path('answer', views.AnswersView.as_view(), name='answer'),
]
urlpatterns.extend(router.urls)