# Generated by Django 4.2.7 on 2024-05-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0019_website_image_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='website_image',
            name='Name',
            field=models.ImageField(default=None, upload_to='webImages'),
        ),
    ]
