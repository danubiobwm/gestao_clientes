# Generated by Django 2.0.1 on 2019-07-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20190704_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='desconto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='venda',
            name='impostos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
