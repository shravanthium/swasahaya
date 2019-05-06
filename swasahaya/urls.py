from django.urls import path, include, re_path

from django.contrib import admin

admin.autodiscover()

import bank.views
import bank.api

bank_list = bank.api.BankViewSet.as_view({'get': 'list'})
bank_detail = bank.api.BankViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('', bank.views.HomePageView.as_view(), name='index'),
    path('banks/', bank_list, name='bank_list'),
    re_path(r'^banks/(?P<ifsc_code>\w+)/$', bank_detail, name='bank_detail'),
    path("admin/", admin.site.urls),
]