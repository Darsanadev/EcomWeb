# Generated by Django 4.2.4 on 2024-06-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_delete_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='offer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]