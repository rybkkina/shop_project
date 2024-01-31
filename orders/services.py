from cart.cart import Cart
from orders.models import Order, OrderItem
from .tasks import order_created


class CreateOrderService:
    def __init__(self, cart: Cart):
        self.cart = cart

    def create_order(
            self,
            first_name: str,
            last_name: str,
            email: str,
            address: str,
            postal_code: str,
            city: str,
    ) -> Order:
        order = Order.objects.create(
            first_name=first_name, last_name=last_name, email=email, address=address,
            postal_code=postal_code, city=city,
        )
        if self.cart.coupon:
            order.coupon = self.cart.coupon
            order.discount = self.cart.coupon.discount
            order.save()
        for item in self.cart:
            OrderItem.objects.create(
                order=order, product=item['product'], price=item['price'], quantity=item['quantity'],
            )
        self.cart.clear()
        # launch asynchronous task
        order_created.delay(order.id)  # set the order in the session
        return order
