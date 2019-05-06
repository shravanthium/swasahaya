from django.shortcuts import render
from django.views import generic

from bank.models import *

class HomePageView(generic.ListView):
    model = Bank
    template_name = 'index.html'
    context_object_name = 'banks'

    def get_queryset(self):
        return Bank.objects.all()[:15]