# Generated by Django 4.2.4 on 2024-05-30 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0013_remove_account_address_remove_account_city_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Useraccount',
        ),
    ]