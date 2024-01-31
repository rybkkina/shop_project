from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cart.api.v1.serializer import CartSerializer
from shop.models import Product
from cart.cart import Cart
from shop.permissions import IsAdminOrReadOnly


class CartAPIView(APIView):
    def get(self, request):
        #cart = request.session.get('cart', {})
        cart = request.session.get(settings.CART_SESSION_ID)
        product_ids = list(cart.keys())
        products = Product.objects.filter(id__in=product_ids)
        serializer = CartSerializer(products, many=True)
        return Response(serializer.data)


    def post(self, request):
        product_id = int(request.data.get('product_id'))
        product = Product.objects.get(id=product_id)
        Cart(request).add(product, quantity=1, override_quantity=False)
        return Response({"success": "Product added to cart"}, status=status.HTTP_201_CREATED)

    def delete(self, request):
        product_id = request.data.get('product_id')
        removed = Cart(request).remove(str(product_id))
        if removed:
            return Response({"success": "Product removed from cart"}, status=status.HTTP_200_OK)
        return Response({"error": "Product not found in cart"}, status=status.HTTP_404_NOT_FOUND)

    # permission_classes = [IsAdminOrReadOnly]




''' def post(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        cart = request.session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + 1
        request.session['cart'] = cart
        request.session.modified = True
        return Response({"success": "Product added to cart"}, status=status.HTTP_201_CREATED)

    def delete(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        cart = request.session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart
            request.session.modified = True
            return Response({"success": "Product removed from cart"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Product not found in cart"}, status=status.HTTP_404_NOT_FOUND)'''
