# Generated by Django 4.2.4 on 2024-05-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0008_register_alter_otp_username_delete_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]