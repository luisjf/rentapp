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
    property = serializers.SerializerMethodField()
    class Meta:
        model = Local
        fields = [
            'id',
            'property',
            'name',
            'area_total',
            'aliquot'
            ]
    def get_property(self, obj):
        return str(obj.property.name)

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
    property = serializers.SerializerMethodField()
    local = serializers.SerializerMethodField()
    tenant = serializers.SerializerMethodField()
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
    def get_property(self, obj):
        return str(obj.property.name)
    def get_local(self, obj):
        return str(obj.local.name)
    def get_tenant(self, obj):
        return str(obj.tenant.first_name + obj.tenant.last_name)

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
            'payment_date',
            'way_to_pay',
            'number',
            'detail'
            ]

class PaymentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'contract',
            'payment_date',
            'way_to_pay',
            'number',
            'detail'
            ]
