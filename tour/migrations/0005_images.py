# Generated by Django 4.2.7 on 2024-04-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_place_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='viewImages')),
            ],
        ),
    ]
