from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('shop.urls', namespace='shop')),
]

urlpatterns += [
    path("api/v1/shop/", include("shop.api.v1.urls")),
    path("api/v1/orders/", include("orders.api.v1.urls")),
    path("api/v1/accounts/", include("accounts.api.v1.urls")),
    path("api/v1/coupons/", include("coupons.api.v1.urls")),
    path("api/v1/cart/", include("cart.api.v1.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)