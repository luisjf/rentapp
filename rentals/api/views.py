from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )

from rentals.models import Tenant, Property, Local, Contract, Payment
from .serializers import TenantSerializer, PropertySerializer, LocalSerializer, ContractSerializer, PaymentSerializer


#TENANT Views

class TenantListAPIView(ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantDetailAPIView(RetrieveAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    #lookup_field = ""

class TenantUpdateAPIView(UpdateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantDeleteAPIView(DestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


#PROPERTY Views

class PropertyListAPIView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailAPIView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    #lookup_field = ""

class PropertyUpdateAPIView(UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDeleteAPIView(DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


#LOCAL Views

class LocalListAPIView(ListAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalDetailAPIView(RetrieveAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
    #lookup_field = ""

class LocalUpdateAPIView(UpdateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

class LocalDeleteAPIView(DestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


#CONTRACT Views

class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class ContractDetailAPIView(RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    #lookup_field = ""

class ContractUpdateAPIView(UpdateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class ContractDeleteAPIView(DestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


#PAYMENT Views

class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    #lookup_field = ""

class PaymentUpdateAPIView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDeleteAPIView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
