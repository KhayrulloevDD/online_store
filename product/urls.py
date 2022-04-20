from django.urls import path, include
from product import apis
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product', apis.ProductViewSet)
router.register('order', apis.OrderViewSet)
router.register('order_item', apis.OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
