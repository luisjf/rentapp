from django.conf.urls import url
from django.contrib import admin

from rentals.api.views import (
    TenantListAPIView,
    TenantDetailAPIView,

    PropertyListAPIView,
    LocalListAPIView,
    ContractListAPIView,
    PaymentListAPIView
)

urlpatterns = [
    url(r'^tenant/$', TenantListAPIView.as_view(), name='list'),
    url(r'^tenant/(?P<pk>)\d/$', TenantDetailAPIView.as_view(), name='detail'),


    url(r'^property/$', PropertyListAPIView.as_view()),
    url(r'^local/$', LocalListAPIView.as_view()),
    url(r'^contract/$', ContractListAPIView.as_view()),
    url(r'^payment/$', PaymentListAPIView.as_view()),
]
