# Generated by Django 4.2.4 on 2024-05-24 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_listed', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='media')),
                ('is_listed', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('landing_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('selling_price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_listed', models.BooleanField(blank=True, default=True, null=True)),
                ('brand', models.ForeignKey(default='someee string', on_delete=django.db.models.deletion.CASCADE, to='backend.brand')),
                ('category', models.ForeignKey(default='somee string', on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
            ],
        ),
    ]