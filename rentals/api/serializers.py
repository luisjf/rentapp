from rentals.models import Contract, Local, Payment, Property, Tenant
from rest_framework import serializers

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id_card_prefix', 'id_card', 'first_name', 'last_name', 'birthdate', 'local_phone_area', 'local_phone', 'mobile_phone_area', 'mobile_phone', 'work_phone_area', 'work_phone', 'billing_address')

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ()

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ()

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ()

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ()
