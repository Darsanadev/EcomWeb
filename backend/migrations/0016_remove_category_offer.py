# Generated by Django 4.2.4 on 2024-06-16 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_category_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='offer',
        ),
    ]
