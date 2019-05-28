from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import FieldDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = models.User.objects.all()
        filter_by_name = self.request.GET.get('name')
        order_by_field = self.request.GET.get('sort')
        if filter_by_name:
            queryset = models.User.objects.filter(
                Q(first_name__icontains=filter_by_name) |
                Q(last_name__icontains=filter_by_name))
        if order_by_field:
            try:
                models.User._meta.get_field(order_by_field.replace('-', ''))
                queryset = queryset.order_by(order_by_field)
            except FieldDoesNotExist:
                pass
        return queryset

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=201)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=200)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        super().update(request, *args, **kwargs)
        return Response(status=200)
