from django.conf.urls import url
from django.contrib import admin

from rentals.api.views import (

    TenantListAPIView,
    TenantDetailAPIView,
    TenantUpdateAPIView,
    TenantDeleteAPIView,

    PropertyListAPIView,
    PropertyDetailAPIView,
    PropertyUpdateAPIView,
    PropertyDeleteAPIView,

    LocalListAPIView,
    LocalDetailAPIView,
    LocalUpdateAPIView,
    LocalDeleteAPIView,

    ContractListAPIView,
    ContractDetailAPIView,
    ContractUpdateAPIView,
    ContractDeleteAPIView,

    PaymentListAPIView,
    PaymentDetailAPIView,
    PaymentUpdateAPIView,
    PaymentDeleteAPIView
)

urlpatterns = [
    url(r'^tenant/$', TenantListAPIView.as_view(), name='list'),
    url(r'^tenant/(?P<pk>[\w-]+)/$', TenantDetailAPIView.as_view(), name='detail'),
    url(r'^tenant/(?P<pk>[\w-]+)/edit/$', TenantUpdateAPIView.as_view(), name='update'),
    url(r'^tenant/(?P<pk>[\w-]+)/delete/$', TenantDeleteAPIView.as_view(), name='delete'),


    url(r'^property/$', PropertyListAPIView.as_view()),
    url(r'^property/(?P<pk>[\w-]+)/$', PropertyDetailAPIView.as_view(), name='detail'),
    url(r'^property/(?P<pk>[\w-]+)/edit/$', PropertyUpdateAPIView.as_view(), name='update'),
    url(r'^property/(?P<pk>[\w-]+)/delete/$', PropertyDeleteAPIView.as_view(), name='delete'),

    url(r'^local/$', LocalListAPIView.as_view()),
    url(r'^local/(?P<pk>[\w-]+)/$', LocalDetailAPIView.as_view(), name='detail'),
    url(r'^local/(?P<pk>[\w-]+)/edit/$', LocalUpdateAPIView.as_view(), name='update'),
    url(r'^local/(?P<pk>[\w-]+)/delete/$', LocalDeleteAPIView.as_view(), name='delete'),

    url(r'^contract/$', ContractListAPIView.as_view()),
    url(r'^contract/(?P<pk>[\w-]+)/$', ContractDetailAPIView.as_view(), name='detail'),
    url(r'^contract/(?P<pk>[\w-]+)/edit/$', ContractUpdateAPIView.as_view(), name='update'),
    url(r'^contract/(?P<pk>[\w-]+)/delete/$', ContractDeleteAPIView.as_view(), name='delete'),

    url(r'^payment/$', PaymentListAPIView.as_view()),
    url(r'^payment/(?P<pk>[\w-]+)/$', PaymentDetailAPIView.as_view(), name='detail'),
    url(r'^payment/(?P<pk>[\w-]+)/edit/$', PaymentUpdateAPIView.as_view(), name='update'),
    url(r'^payment/(?P<pk>[\w-]+)/delete/$', PaymentDeleteAPIView.as_view(), name='delete'),
]
