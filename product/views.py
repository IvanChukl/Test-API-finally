# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from . import serializers
from . import models

class FlowersViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.FlowersSerializer
    queryset = models.Flower.objects.all()
    filters_backends = (filters.SearchFilter,)
    search_fields = ('categories', 'price',)

class GiftsViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.GiftsSerializer
    queryset = models.Gift.objects.all()
    filters_backends = (filters.SearchFilter,)
    search_fields = ('categories', 'price',)
