# Generated by Django 5.0.6 on 2024-06-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debt_manager', '0012_rename_debtors_debt_debtor_alter_debt_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='is_hidden',
            field=models.BooleanField(default=False, verbose_name='Скрыто'),
        ),
        migrations.AlterField(
            model_name='debt',
            name='currency',
            field=models.CharField(choices=[('BYN', 'BYN'), ('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=200, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='exchangerate',
            name='currency',
            field=models.CharField(choices=[('BYN', 'BYN'), ('USD', 'USD'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=200, verbose_name='Валюта'),
        ),
    ]