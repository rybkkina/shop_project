from rest_framework import serializers
from coupons.models import Coupon


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'