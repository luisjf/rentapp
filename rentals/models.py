from __future__ import unicode_literals

from django.db import models

"""

Entidades:

tenant (Inquilino)
property (Inmueble)
local (Local)
contract (Contrato)
payment (Pago)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

"""
#Inquilino
class Tenant(models.Model):
    ID_CARD_CHOICES = (
        ('1', 'V'),
        ('2', 'E'),
        ('3', 'J'),
        ('4', 'G'),
    )
    id_card_prefix = models.CharField(max_length=10, choices=ID_CARD_CHOICES)
    id_card = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    local_phone_area = models.CharField(max_length=25)
    local_phone = models.CharField(max_length=50)
    mobile_phone_area = models.CharField(max_length=25)
    mobile_phone = models.CharField(max_length=50)
    work_phone_area = models.CharField(max_length=25)
    work_phone = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=1000)

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class Local(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area_total = models.IntegerField()
    aliquot = models.IntegerField()

class Contract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    payment_day = models.IntegerField()
    payment_due_day = models.IntegerField()

class Payment(models.Model):
    WAY_TO_PAY_CHOICES = (
        ('1', 'Efectivo'),
        ('2', 'Deposito Bancario'),
        ('3', 'Transferencia'),
        ('4', 'Cheque'),
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    payment_date = models.DateField()
    way_to_pay = models.CharField(max_length=10, choices=WAY_TO_PAY_CHOICES)
    number = models.CharField(max_length=50)
    detail = models.CharField(max_length=1000)
