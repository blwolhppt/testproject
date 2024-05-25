from rest_framework import viewsets

from shop.models import Organization, Shop
from api import serializers


class OrganizationsViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationsSerializer


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = serializers.ShopsSerializer

