# from django.conf.urls import url
from django.urls import path
# from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views
# router = DefaultRouter()

router = routers.SimpleRouter()
router.register(r'users', views.AnswersView)
urlpatterns = router.urls
# router.register(r'answer', views.AnswersView, 'answer-base')
# urlpatterns = [
# ]
# urlpatterns.extend(router.urls)
