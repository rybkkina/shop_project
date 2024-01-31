from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("users", UserViewSet)


urlpatterns = [
    path("login_api", LoginAPIView.as_view()),
]
urlpatterns += router.urls
