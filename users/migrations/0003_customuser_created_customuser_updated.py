# Generated by Django 5.1 on 2024-08-12 06:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
