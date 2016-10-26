from rest_framework.generics import ListAPIView, RetrieveAPIView

from rentals.models import Tenant, Property, Local, Contract, Payment
from .serializers import TenantSerializer, PropertySerializer, LocalSerializer, ContractSerializer, PaymentSerializer

class TenantListAPIView(ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantDetailAPIView(RetrieveAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class PropertyListAPIView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class LocalListAPIView(ListAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
