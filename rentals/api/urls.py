from django.conf.urls import url
from django.contrib import admin

from rentals.api.views import (
    TenantListAPIView,
    PropertyListAPIView,
    LocalListAPIView,
    ContractListAPIView,
    PaymentListAPIView
)

urlpatterns = [
    url(r'^tenant/$', TenantListAPIView.as_view()),
    url(r'^property/$', PropertyListAPIView.as_view()),
    url(r'^local/$', LocalListAPIView.as_view()),
    url(r'^contract/$', ContractListAPIView.as_view()),
    url(r'^payment/$', PaymentListAPIView.as_view()),
]
