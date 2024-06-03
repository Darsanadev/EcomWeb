# Generated by Django 4.2.4 on 2024-05-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0015_delete_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Useraccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]