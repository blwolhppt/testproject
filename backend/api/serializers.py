from shop.models import Organization, Shop

from rest_framework import serializers


class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
