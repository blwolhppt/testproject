from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from shop.models import Organization, Shop
from api import serializers

from django.core.mail import send_mail
from api.send_email import send_email_task


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

    http_method_names = ['get', 'put']


    def update(self, request, pk):
        shop = get_object_or_404(Shop, id=pk)
        serializer = serializers.ShopsSerializer(shop, data=request.data)
        send_email_task()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
