# Generated by Django 4.2.4 on 2024-06-08 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0021_register_otp_delete_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='otp',
            new_name='otpcode',
        ),
    ]