# Generated by Django 4.2.4 on 2024-06-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0038_cart_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_status',
            field=models.IntegerField(choices=[(2, 'ORDER_PROCESSED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED')], default=((2, 'ORDER_PROCESSED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED'))),
        ),
    ]
