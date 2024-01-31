from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("orders", OrderViewSet)
router.register("orderitems", OrderItemViewSet)

urlpatterns = [
]
urlpatterns += router.urls
