from rentals.models import Contract, Local, Payment, Property, Tenant
from rest_framework import serializers

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = [
            'id',
            'id_card_prefix',
            'id_card',
            'first_name',
            'last_name',
            'birthdate',
            'local_phone_area',
            'local_phone',
            'mobile_phone_area',
            'mobile_phone',
            'work_phone_area',
            'work_phone',
            'billing_address'
            ]

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'name',
            'address'
            ]

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = [
            'id',
            'property',
            'name',
            'area_total',
            'aliquot'
            ]

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id',
            'tenant',
            'local',
            'property',
            'issue_date',
            'due_date',
            'payment_day',
            'payment_due_day'
            ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'contract',
            'payment_day',
            'way_to_pay',
            'number',
            'detail'
            ]
