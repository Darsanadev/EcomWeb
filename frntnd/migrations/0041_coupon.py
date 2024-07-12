# Generated by Django 4.2.4 on 2024-06-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0040_alter_cart_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=50, unique=True)),
                ('discount', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateField()),
            ],
        ),
    ]
