from django.db import models

# Create your models here.


# class Bill(models.Model):
#     name = models.CharField(max_length=256, verbose_name="Название", choices=BILLS_CHOICES)
#     description = models.TextField(verbose_name='Описание', blank=True, null=True)
#     amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма', blank=True, null=True)
#     payment_date = models.DateField(verbose_name='Дата платежа')
#
#     def __str__(self):
#         return f"{self.payment_date} {self.name} - {self.amount}"
#
#     class Meta:
#         verbose_name = "Платеж"
#         verbose_name_plural = "Платежи"
#         ordering = ('-payment_date',)


class Rent(models.Model):
    title = 'Квартплата'
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма')
    payment_date = models.DateField(verbose_name='Дата платежа')

    def __str__(self):
        return f"{self.payment_date} - {self.amount} руб."

    class Meta:
        verbose_name = 'Квартплата'
        verbose_name_plural = 'Квартплата'
        ordering = ('-payment_date',)


class Gas(models.Model):
    title = 'Газ'
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    indications = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Показания', max_length=120)
    payment_date = models.DateField(verbose_name='Дата платежа')

    def __str__(self):
        return f"{self.payment_date} - {self.indications}"

    class Meta:
        verbose_name = 'Газ'
        verbose_name_plural = 'Газ'
        ordering = ('-payment_date',)


class ColdWater(models.Model):
    title = 'Холодная вода'
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    indications = models.IntegerField(verbose_name='Показания')
    payment_date = models.DateField(verbose_name='Дата платежа')

    def __str__(self):
        return f"{self.payment_date} - {self.indications}"

    class Meta:
        verbose_name = 'Холодная вода'
        verbose_name_plural = 'Холодная вода'
        ordering = ('-payment_date',)


class HotWater(models.Model):
    title = 'Горячая вода'
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    indications = models.IntegerField(verbose_name='Показания')
    payment_date = models.DateField(verbose_name='Дата платежа')

    def __str__(self):
        return f"{self.payment_date} - {self.indications}"

    class Meta:
        verbose_name = 'Горячая вода'
        verbose_name_plural = 'Горячая вода'
        ordering = ('-payment_date',)


class Electricity(models.Model):
    title = 'Электроэнергия'
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    indications = models.IntegerField(verbose_name='Показания', max_length=120)
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма', blank=True, null=True)
    rate = models.DecimalField(max_digits=5, decimal_places=4, verbose_name='Тариф')
    payment_date = models.DateField(verbose_name='Дата платежа')

    def __str__(self):
        return f"{self.payment_date} - {self.indications}"

    class Meta:
        verbose_name = 'Электроэнергия'
        verbose_name_plural = 'Электроэнергия'
        ordering = ('-payment_date',)


