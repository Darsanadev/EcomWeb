# Generated by Django 4.2.4 on 2024-05-27 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0004_cart_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='username',
            new_name='user',
        ),
    ]
