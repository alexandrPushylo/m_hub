# Generated by Django 5.0.6 on 2024-05-29 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debt_manager', '0009_rename_debtors_debtor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Название'),
        ),
    ]
