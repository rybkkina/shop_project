from rest_framework import mixins
from rest_framework import viewsets

from shop.permissions import IsAdminOrReadOnly
from .serializer import OrderSerializer, OrderItemSerializer
from ...models import Order, OrderItem


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]



class OrderItemViewSet(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminOrReadOnly]

