from rest_framework import routers
from .api import ExecutorViewSet, SpecialityViewSet, ExecutorCommentsViewSet, ExecutorAPIDetailView
from django.urls import path

router = routers.DefaultRouter()
router.register('api/executor', ExecutorViewSet, 'executor')
router.register('api/speciality', SpecialityViewSet, 'speciality')
router.register('api/executor_comments', ExecutorCommentsViewSet, 'executor_comments')


urlpatterns = [path('api/detailexecutor/<int:pk>/', ExecutorAPIDetailView.as_view())]
urlpatterns += router.urls

