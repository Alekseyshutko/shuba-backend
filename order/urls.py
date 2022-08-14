from django.urls import path
from rest_framework import routers
from .api import OrderViewSet, OrderCommentsViewSet, OrderPhotosViewSet, SpecialityOrderViewSet, OrderAPIDetailView

router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'order')
router.register('api/specialityorder', SpecialityOrderViewSet, 'specialityorder')
router.register('api/order_comments', OrderCommentsViewSet, 'order_comments')
router.register('api/orderphotos', OrderPhotosViewSet, 'orderphotos')


urlpatterns = [path('api/detailorder/<int:pk>/', OrderAPIDetailView.as_view())

]
urlpatterns += router.urls




