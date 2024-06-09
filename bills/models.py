from django.db import models
from m_hub.assets import BILLS_CHOICES

# Create your models here.


class Bill(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название", choices=BILLS_CHOICES)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма', blank=True, null=True)
    payment_date = models.DateField(verbose_name='Дата платежа')

    def __str__(self):
        return f"{self.payment_date} {self.name} - {self.amount}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ('-payment_date',)
