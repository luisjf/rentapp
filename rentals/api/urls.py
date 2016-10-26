from django.conf.urls import url
from django.contrib import admin

from rentals.api.views import (

    TenantListAPIView,
    TenantDetailAPIView,

    PropertyListAPIView,
    PropertyDetailAPIView,

    LocalListAPIView,
    LocalDetailAPIView,

    ContractListAPIView,
    ContractDetailAPIView,

    PaymentListAPIView,
    PaymentDetailAPIView
)

urlpatterns = [
    url(r'^tenant/$', TenantListAPIView.as_view(), name='list'),
    url(r'^tenant/(?P<pk>[\w-]+)/$', TenantDetailAPIView.as_view(), name='detail'),


    url(r'^property/$', PropertyListAPIView.as_view()),
    url(r'^property/(?P<pk>[\w-]+)/$', PropertyDetailAPIView.as_view(), name='detail'),

    url(r'^local/$', LocalListAPIView.as_view()),
    url(r'^local/(?P<pk>[\w-]+)/$', LocalDetailAPIView.as_view(), name='detail'),

    url(r'^contract/$', ContractListAPIView.as_view()),
    url(r'^contract/(?P<pk>[\w-]+)/$', ContractDetailAPIView.as_view(), name='detail'),

    url(r'^payment/$', PaymentListAPIView.as_view()),
    url(r'^payment/(?P<pk>[\w-]+)/$', PaymentDetailAPIView.as_view(), name='detail'),
]
