# Generated by Django 4.2.4 on 2024-07-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_product_offer'),
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
