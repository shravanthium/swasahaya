from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginateBy20(PageNumberPagination):
    page_size = 20


class PaginateBy15(PageNumberPagination):
    page_size = 15


class PaginateBy10(PageNumberPagination):
    page_size = 10


class PaginateBy2(PageNumberPagination):
    page_size = 2
