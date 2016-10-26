from rest_framework.generics import ListAPIView, RetrieveAPIView

from rentals.models import Tenant, Property, Local, Contract, Payment
from .serializers import TenantSerializer, PropertySerializer, LocalSerializer, ContractSerializer, PaymentSerializer

class TenantListAPIView(ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantDetailAPIView(RetrieveAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    #lookup_field = ""

class PropertyListAPIView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailAPIView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    #lookup_field = ""

class LocalListAPIView(ListAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalDetailAPIView(RetrieveAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    #lookup_field = ""

class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class ContractDetailAPIView(RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    #lookup_field = ""

class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    #lookup_field = ""
