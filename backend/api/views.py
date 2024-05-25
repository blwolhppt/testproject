from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from shop.models import Organization, Shop
from api import serializers


class OrganizationsViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationsSerializer

    @action(
        detail=True,
        methods=('GET',),
        url_path='shops_file'
    )
    def download_shopsinorganizations(self, request, pk=None):
        shops = Shop.objects.filter(organization_id=pk)
        validate_data = serializers.DownloadSerializer(shops, many=True)

        df = pd.DataFrame(validate_data.data)

        output = BytesIO()
        df.to_csv(output, index=False, sep=';', encoding='cp1251')

        output.seek(0)

        response = HttpResponse(output, content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename=shops.csv'

        return response


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = serializers.ShopsSerializer

    # http_method_names = ['get', 'put', 'delete', 'patch']
