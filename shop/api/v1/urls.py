from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("products", ProductViewSet)
router.register("cat", CategoryViewSet)


urlpatterns = [
]
urlpatterns += router.urls
