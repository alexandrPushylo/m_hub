# Generated by Django 5.0.6 on 2024-06-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debt_manager', '0011_alter_debt_options_alter_debtor_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debt',
            old_name='debtors',
            new_name='debtor',
        ),
        migrations.AlterField(
            model_name='debt',
            name='currency',
            field=models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('BYN', 'BYN'), ('RUB', 'RUB')], max_length=200, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='exchangerate',
            name='currency',
            field=models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('BYN', 'BYN'), ('RUB', 'RUB')], max_length=200, verbose_name='Валюта'),
        ),
    ]
