from decimal import Decimal

import stripe
from django.conf import settings

from orders.models import Order


class PayOrderService:
    def pay_for_order(self, order_id, success_url, cancel_url):
        order = Order.objects.get(id=order_id)
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': settings.SUCCESS_PAYMENT_URL,
            'cancel_url': settings.CANCELLED_PAYMENT_URL,
            'line_items': []
        }
        # add order items to the Stripe checkout session
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })

        if order.coupon:
            stripe_coupon = stripe.Coupon.create(
                name=order.coupon.code,
                percent_off=order.discount,
                duration='once')
            session_data['discounts'] = [{
                'coupon': stripe_coupon.id
            }]
        session = stripe.checkout.Session.create(**session_data)
        return session.url
