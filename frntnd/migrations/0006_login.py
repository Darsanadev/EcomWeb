# Generated by Django 4.2.4 on 2024-05-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0005_rename_username_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
