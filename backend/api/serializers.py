from rest_framework.fields import SerializerMethodField
from shop.models import Organization, Shop

from rest_framework import serializers


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'description', 'address', 'index')


class OrganizationsSerializer(serializers.ModelSerializer):
    shops = SerializerMethodField()

    class Meta:
        model = Organization
        fields = ('name', 'description', 'shops')

    def get_shops(self, organization):
        shops = Shop.objects.filter(organization_id=organization.id,
                                    is_deleted=False)
        return ShopsSerializer(shops, many=True).data
