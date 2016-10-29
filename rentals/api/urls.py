from django.conf.urls import url
from django.contrib import admin

from rentals.api.views import (

    TenantListAPIView,
    TenantDetailAPIView,
    TenantUpdateAPIView,
    TenantDeleteAPIView,
    TenantCreateAPIView,

    PropertyListAPIView,
    PropertyDetailAPIView,
    PropertyUpdateAPIView,
    PropertyDeleteAPIView,
    PropertyCreateAPIView,

    LocalListAPIView,
    LocalDetailAPIView,
    LocalUpdateAPIView,
    LocalDeleteAPIView,
    LocalCreateAPIView,

    ContractListAPIView,
    ContractDetailAPIView,
    ContractUpdateAPIView,
    ContractDeleteAPIView,
    ContractCreateAPIView,

    PaymentListAPIView,
    PaymentDetailAPIView,
    PaymentUpdateAPIView,
    PaymentDeleteAPIView,
    PaymentCreateAPIView
)

urlpatterns = [
    url(r'^tenant/$', TenantListAPIView.as_view(), name='list'),
    url(r'^tenant/create/$', TenantCreateAPIView.as_view(), name='create'),
    url(r'^tenant/(?P<pk>[\w-]+)/$', TenantDetailAPIView.as_view(), name='detail'),
    url(r'^tenant/(?P<pk>[\w-]+)/edit/$', TenantUpdateAPIView.as_view(), name='update'),
    url(r'^tenant/(?P<pk>[\w-]+)/delete/$', TenantDeleteAPIView.as_view(), name='delete'),


    url(r'^property/$', PropertyListAPIView.as_view(), name='list'),
    url(r'^property/create/$', PropertyCreateAPIView.as_view(), name='create'),
    url(r'^property/(?P<pk>[\w-]+)/$', PropertyDetailAPIView.as_view(), name='detail'),
    url(r'^property/(?P<pk>[\w-]+)/edit/$', PropertyUpdateAPIView.as_view(), name='update'),
    url(r'^property/(?P<pk>[\w-]+)/delete/$', PropertyDeleteAPIView.as_view(), name='delete'),

    url(r'^local/$', LocalListAPIView.as_view(), name='list'),
    url(r'^local/create/$', LocalCreateAPIView.as_view(), name='create'),
    url(r'^local/(?P<pk>[\w-]+)/$', LocalDetailAPIView.as_view(), name='detail'),
    url(r'^local/(?P<pk>[\w-]+)/edit/$', LocalUpdateAPIView.as_view(), name='update'),
    url(r'^local/(?P<pk>[\w-]+)/delete/$', LocalDeleteAPIView.as_view(), name='delete'),

    url(r'^contract/$', ContractListAPIView.as_view(), name='list'),
    url(r'^contract/create/$', ContractCreateAPIView.as_view(), name='create'),
    url(r'^contract/(?P<pk>[\w-]+)/$', ContractDetailAPIView.as_view(), name='detail'),
    url(r'^contract/(?P<pk>[\w-]+)/edit/$', ContractUpdateAPIView.as_view(), name='update'),
    url(r'^contract/(?P<pk>[\w-]+)/delete/$', ContractDeleteAPIView.as_view(), name='delete'),

    url(r'^payment/$', PaymentListAPIView.as_view(), name='list'),
    url(r'^payment/create/$', PaymentCreateAPIView.as_view(), name='create'),
    url(r'^payment/(?P<pk>[\w-]+)/$', PaymentDetailAPIView.as_view(), name='detail'),
    url(r'^payment/(?P<pk>[\w-]+)/edit/$', PaymentUpdateAPIView.as_view(), name='update'),
    url(r'^payment/(?P<pk>[\w-]+)/delete/$', PaymentDeleteAPIView.as_view(), name='delete'),
]
    
