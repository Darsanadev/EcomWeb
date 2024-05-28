# Generated by Django 4.2.4 on 2024-05-28 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frntnd', '0006_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='username',
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frntnd.login')),
            ],
        ),
    ]
