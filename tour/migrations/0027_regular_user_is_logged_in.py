# Generated by Django 4.2.7 on 2024-06-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0026_regular_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='regular_user',
            name='is_logged_in',
            field=models.BooleanField(default=False),
        ),
    ]