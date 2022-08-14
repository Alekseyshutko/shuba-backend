from rest_framework.response import Response

from .models import Order, OrderComments, OrderPhotos, SpecialityOrder
from rest_framework import viewsets, permissions, generics
from .serializers import OrderSerializer, OrderCommentsSerializer, OrderPhotosSerializer, SpecialityOrderSerializer, \
    DeleteOrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['speciality']

    # def create(self, request, *args, **kwargs):
    #     # import pdb
    #     # pdb.set_trace()
    #     return super(OrderViewSet, self).create(reqeust, *args)


class SpecialityOrderViewSet(viewsets.ModelViewSet):
    queryset = SpecialityOrder.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SpecialityOrderSerializer


class OrderCommentsViewSet(viewsets.ModelViewSet):
    queryset = OrderComments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderCommentsSerializer


class OrderPhotosViewSet(viewsets.ModelViewSet):
    queryset = OrderPhotos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderPhotosSerializer


class OrderAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
