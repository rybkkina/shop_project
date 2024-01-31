from django.urls import path

from .views import *

#router = SimpleRouter()
#router.register()

urlpatterns = [
    path("cart", CartAPIView.as_view()),
]
#urlpatterns += router.urls
