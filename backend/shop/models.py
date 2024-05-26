from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name='Название организации')

    description = models.TextField(max_length=350,
                                   verbose_name='Описание организации')

    class Meta:
        verbose_name = 'Организация'

    def __str__(self):
        return self.name


class Shop(models.Model):
    organization_id = models.ForeignKey(Organization,
                                        on_delete=models.CASCADE,
                                        verbose_name='Организация')
    name = models.CharField(max_length=150,
                            verbose_name='Название магазина')

    description = models.TextField(max_length=350,
                                   verbose_name='Описание магазина')
    address = models.CharField(max_length=200,
                               verbose_name='Адрес')
    index = models.IntegerField(verbose_name='Индекс')
    is_deleted = models.BooleanField()

    class Meta:
        verbose_name = 'Магазин'

    def __str__(self):
        return self.name
