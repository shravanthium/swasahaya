from django.shortcuts import get_object_or_404

from rest_framework import views, status, generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Bank
from .serializers import BankSerializer
from .paginations import PaginateBy20

class BankViewSet(viewsets.ViewSet):
    """
    retrieve:
    Given a bank branch IFSC code, get branch details
    list:
    Given a bank name and city, gets details of all branches of the bank in the city
    """
    permission_classes = (AllowAny, )
    pagination_class = PaginateBy20

    def list(self, request):
        queryset = Bank.objects.all()
        city = self.request.query_params.get('city', None)
        bank_name = self.request.query_params.get('bank_name', None)
        if city is not None and bank_name is not None:
            queryset = queryset.filter(city=city,bank_name=bank_name)
        serializer = BankSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, ifsc_code=None):
        print(ifsc_code)
        bank = get_object_or_404(Bank, ifsc=ifsc_code)
        serializer = BankSerializer(bank)
        return Response(serializer.data)