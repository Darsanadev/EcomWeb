# Generated by Django 4.2.4 on 2024-05-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_brand_description_alter_brand_is_listed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='is_listed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
