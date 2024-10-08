# Generated by Django 5.1 on 2024-08-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_gamescore_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='settings',
            field=models.TextField(default='default_settings'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamescore',
            name='game',
            field=models.TextField(choices=[('MATH', 'Math Facts'), ('ANAGRAM', 'Anagram Hunt')], default='MATH'),
        ),
    ]
