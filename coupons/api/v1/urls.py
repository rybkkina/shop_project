from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("coupons", CouponsViewSet)

urlpatterns = [
]
urlpatterns += router.urls
