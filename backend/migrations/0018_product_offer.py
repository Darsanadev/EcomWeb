# Generated by Django 4.2.4 on 2024-06-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_brand_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
