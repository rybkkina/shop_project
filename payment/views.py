import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404

from orders.models import Order
from payment.services import PayOrderService

# create the Stripe instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get('order_id', None)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        payment_url = PayOrderService().pay_for_order(order_id, success_url, cancel_url)
        # redirect to Stripe payment form
        return redirect(payment_url, code=303)

    order = get_object_or_404(Order, id=order_id)
    return render(
        request,
        'payment/process.html',
        {"request": request, "order_id": order_id, "order": order}
    )


def payment_completed(request):
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
