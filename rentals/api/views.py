from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
    )

from rentals.models import Tenant, Property, Local, Contract, Payment
from .serializers import (

    TenantListSerializer,
    TenantDetailSerializer,
    TenantCreateUpdateSerializer,

    PropertyDetailSerializer,
    PropertyCreateUpdateSerializer,

    LocalDetailSerializer,
    LocalCreateUpdateSerializer,

    ContractDetailSerializer,
    ContractCreateUpdateSerializer,

    PaymentDetailSerializer,
    PaymentCreateUpdateSerializer
    )


#TENANT Views

class TenantListAPIView(ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantListSerializer

class TenantDetailAPIView(RetrieveAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantDetailSerializer
    #lookup_field = ""

class TenantCreateAPIView(CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantCreateUpdateSerializer

class TenantUpdateAPIView(UpdateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantCreateUpdateSerializer

class TenantDeleteAPIView(DestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantDetailSerializer


#PROPERTY Views

class PropertyListAPIView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer

class PropertyDetailAPIView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer
    #lookup_field = ""

class PropertyCreateAPIView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateUpdateSerializer

class PropertyUpdateAPIView(UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateUpdateSerializer

class PropertyDeleteAPIView(DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer


#LOCAL Views

class LocalListAPIView(ListAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalDetailSerializer

class LocalDetailAPIView(RetrieveAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalDetailSerializer
    #lookup_field = ""

class LocalCreateAPIView(CreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalCreateUpdateSerializer

class LocalUpdateAPIView(UpdateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalCreateUpdateSerializer

class LocalDeleteAPIView(DestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalDetailSerializer


#CONTRACT Views

class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer

class ContractDetailAPIView(RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer
    #lookup_field = ""

class ContractUpdateAPIView(UpdateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractCreateUpdateSerializer

class ContractCreateAPIView(CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractCreateUpdateSerializer

class ContractDeleteAPIView(DestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer



#PAYMENT Views

class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentDetailSerializer

class PaymentDetailAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentDetailSerializer
    #lookup_field = ""

class PaymentUpdateAPIView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateUpdateSerializer

class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateUpdateSerializer

class PaymentDeleteAPIView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentDetailSerializer
