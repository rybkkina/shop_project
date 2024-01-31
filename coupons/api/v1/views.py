from rest_framework import mixins
from rest_framework import viewsets

from shop.permissions import IsAdminOrReadOnly
from .serializer import CouponsSerializer
from coupons.models import Coupon


class CouponsViewSet(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Coupon.objects.all()
    serializer_class = CouponsSerializer
    permission_classes = [IsAdminOrReadOnly]
