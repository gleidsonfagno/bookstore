
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

class OrderViewset(ModelViewSet):

    queryset_class - OrderSerializer
    queryset = Order.objects.all()