# Generated by Django 4.2.7 on 2024-04-01 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_place_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='offer',
            field=models.CharField(max_length=255, null=True),
        ),
    ]