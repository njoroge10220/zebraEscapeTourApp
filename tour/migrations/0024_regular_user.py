# Generated by Django 4.2.7 on 2024-05-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0023_place_wording'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regular_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('con_password', models.CharField(max_length=100)),
            ],
        ),
    ]
