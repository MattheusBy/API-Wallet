from django.urls import path
from rest_framework import routers
from wallet.views import UserBalanceAPIView, TransactionViewSet

router = routers.SimpleRouter()
router.register(r'transactions', TransactionViewSet)


urlpatterns = [
    path('balance/', UserBalanceAPIView.as_view(), name="set_balance"),
]

urlpatterns += router.urls
