from django.db import models
from m_hub.assets import CURRENCY_CHOICES

# Create your models here.


class Debt(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма', blank=True, null=True)
    currency = models.CharField(max_length=200, verbose_name='Валюта', choices=CURRENCY_CHOICES)
    date_start = models.DateField(verbose_name='Дата создания', blank=True, null=True)
    date_end = models.DateField(verbose_name='Конечная дата', blank=True, null=True)
