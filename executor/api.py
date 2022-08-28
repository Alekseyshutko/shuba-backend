from .models import Executor, Speciality, ExecutorComments
from rest_framework import viewsets, permissions, generics
from .serializers import ExecutorSerializer, SpecialitySerializer, ExecutorCommentsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsExecutorOrReadOnly


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExecutorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['speciality']


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SpecialitySerializer


class ExecutorCommentsViewSet(viewsets.ModelViewSet):
    queryset = ExecutorComments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExecutorCommentsSerializer


class ExecutorAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsExecutorOrReadOnly]


class SpecialityAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speciality.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SpecialitySerializer


