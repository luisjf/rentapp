from rentals.models import Contract, Local, Payment, Property, Tenant
from rest_framework import serializers

#TENANT serializers

class TenantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = [
            'id',
            'id_card_prefix',
            'id_card',
            'first_name',
            'last_name',
            'local_phone_area',
            'local_phone',
            ]

class TenantDetailSerializer(serializers.ModelSerializer):
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

class TenantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = [
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


#PROPERTY serializers

class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'name',
            'address'
            ]

class PropertyCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'name',
            'address'
            ]


#LOCAL serializers

class LocalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = [
            'id',
            'property',
            'name',
            'area_total',
            'aliquot'
            ]

class LocalCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = [
            'property',
            'name',
            'area_total',
            'aliquot'
            ]


#CONTRACT serializers

class ContractDetailSerializer(serializers.ModelSerializer):
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

class ContractCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'tenant',
            'local',
            'property',
            'issue_date',
            'due_date',
            'payment_day',
            'payment_due_day'
            ]


#PAYMENT serializers

class PaymentDetailSerializer(serializers.ModelSerializer):
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

class PaymentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'contract',
            'payment_day',
            'way_to_pay',
            'number',
            'detail'
            ]
